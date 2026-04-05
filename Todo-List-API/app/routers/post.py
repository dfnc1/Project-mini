from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from app.schemas import User, Post
from app.security import get_current_user

router = APIRouter(prefix="/post", tags=["post"])

@router.get("/todos")
async def get_todos(current_user: Annotated[User, Depends(get_current_user)]):
    return {"get"}

@router.get("/todos/{todo_id}")
async def get_todo(todo_id: int, current_user: Annotated[User, Depends(get_current_user)]):
    return f"get_todo {todo_id}"

@router.post("/todos")
async def add_todo(todo: Post, current_user: Annotated[User, Depends(get_current_user)]):
    return todo

@router.put("/todos/{todo_id}")
async def update_todo(todo_id: int, current_user: Annotated[User, Depends(get_current_user)]):
    return f"updated{todo_id}"

@router.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int, current_user: Annotated[User, Depends(get_current_user)]):
    return f"deleted{todo_id}"