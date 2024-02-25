from typing import List
from beanie import PydanticObjectId
from database.connection import Database
from fastapi import APIRouter,HTTPException,status,Request
from models.todo import Todo,TodoUpdate


todo_router=APIRouter(
    prefix='todo'
    tags=['Todos']
)

todo_db=Database(Todo)

@todo_router.post('/')
async def add_todo(request:Request,todo:Todo):
    await todo_db.create(todo)
    # todos=await todo_db.get_all()
    return True

@todo_router.get('/',response_model=List[Todo])
async def get_all_todos_here(request:Request)->List[Todo]:
    todos=await todo_db.get_all()
    return todos  

@todo_router.get('/{id}',response_model=Todo)
async def get_todo_byId(request:Request,id: PydanticObjectId)->Todo:
    todo=await todo_db.get(id)
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Oops, TODO not found :( '
        )
    return todo


@todo_router.put('/{id}',response_model=Todo)
async def update_todo_byId(id: PydanticObjectId,body:TodoUpdate)->Todo:
    updated_todo=await todo_db.update(id,body)
    if not updated_todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Oops, TODO not found :( '
        )
    return updated_todo


@todo_router.delete('/{id}')
async def delete_todo_byId(id: PydanticObjectId)->dict:
    deleted_todo=await todo_db.delete(id)
    if not deleted_todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Oops, TODO not found :( '
        )
    return {"msg":"TODO DROP SUCCESS :)"}
