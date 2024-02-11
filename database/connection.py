
from typing import Any, Optional, List
from beanie import init_beanie, PydanticObjectId
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from pydantic_settings import BaseSettings # NEW
from models.todo import Todo  # Importing the Todo model from another file
import os
from dotenv import load_dotenv

load_dotenv()


# Configuration for database settings
class Settings(BaseModel):
    DATABASE_URL: Optional[str] = None  # Optional URL for the MongoDB database

    async def init_db(self):
        """Initializes the database connection and Beanie ORM."""
        DATABASE_URL = os.getenv('DATABASE_URL')

        client = AsyncIOMotorClient(DATABASE_URL)  # Connect to MongoDB
        await init_beanie(
        database=client.db_name, document_models=[Todo]  # Configure Beanie
        )
        print(DATABASE_URL)
    

    class Config:
        env_file = ".env"  # Load settings from a .env file

# Class for managing database interactions
class Database:
    def __init__(self, model):
        """Initializes the Database class with the specified model."""
        self.model = model  # Store the model class to be used for operations

    async def create(self, document) -> None:
        """Creates a new document in the database."""
        await document.create()  # Call the model's create method

    async def get(self, id: PydanticObjectId) -> Any:
        """Retrieves a document by its ID."""
        doc = await self.model.get(id)  # Query the database using the model's get method
        return doc if doc else False  # Return the document or False if not found

    async def get_all(self) -> List[Any]:
        """Retrieves all documents of the specified model."""
        docs = await self.model.find_all().to_list()  # Fetch all documents and convert to a list
        return docs if docs else False  # Return the list or False if empty

    async def update(self, id: PydanticObjectId, body: BaseModel) -> Any:
        """Updates an existing document with the provided data."""
        doc_id = id
        des_body = {key: value for key, value in body.dict().items() if value is not None}  # Remove None values
        update_query = {"set": des_body}  # Construct the update query
        update_doc = await self.get(doc_id)  # Retrieve the document to update
        if update_doc:
            update_doc.update(update_query)  # Apply the update
            return update_doc  # Return the updated document
        return False  # Return False if document not found

    async def delete(self, id: PydanticObjectId) -> bool:
        """Deletes a document by its ID."""
        doc = await self.get(id)  # Retrieve the document to delete
        if doc:
            await doc.delete()  # Delete the document
            return True  # Return True if successful
        return False  # Return False if document not found

