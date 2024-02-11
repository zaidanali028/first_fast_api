from typing import List
from beanie import PydanticObjectId
from database.connection import Database
from fastapi import APIRouter,HTTPException,status,Request
from models.todo import Todo


todo_router=APIRouter(
    tags=['Todos']
)

todo_db=Database(Todo)

@todo_router.post('/')
async def add_todo(request:Request,todo:Todo):
    await todo_db.create(todo)
    todos=await todo_db.get_all()
    return todos
    
