
# Import the Document class from the beanie library for database interactions with mongodb
from beanie import Document

# Import the BaseModel class from the pydantic library for data models and validation
from pydantic import BaseModel

# Define a model for todo items that will be stored in the database
class Todo(Document):
    # Field for storing the user's name (string type)
    user: str

    # Field for storing the title of the todo item (string type)
    title: str

    # Field for storing a description of the todo item (string type)
    description: str

    # Configuration for providing an example of the model's JSON format
    class Config:
        schema_extra = {
            "example": {
                "user": "Ali Usman Zaidan",
                "title": "My first FAST blog",
                "description": "A Description from FASTAPI"
            }
        }

# Define a model for validating update requests (not directly for database storage)
class TodoUpdate(BaseModel):
    # Optional field for updating the user's name (string or None type)
    user: str | None 

    # Optional field for updating the title of the todo item (string or None type)
    title: str | None 

    # Optional field for updating the description of the todo item (string or None type)
    description: str | None 