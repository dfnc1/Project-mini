from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from app.database import get_db
from app.schemas import User, Post
from app.security import get_current_user
from app.repository.posts import create_post, update_post, delete_post, get_post

router = APIRouter(prefix="/post", tags=["post"])

@router.get("/todos", status_code=status.HTTP_200_OK)
async def get_todos(current_user: Annotated[User, Depends(get_current_user)], conn= Depends(get_db)):
    try:
        return await get_post(conn=conn)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/todos/{todo_id}", status_code=status.HTTP_200_OK)
async def get_todo(todo_id: int, current_user: Annotated[User, Depends(get_current_user)], conn= Depends(get_db)):
    try:
        return await get_post(conn=conn, id=todo_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.post("/todos", status_code=status.HTTP_201_CREATED)
async def add_todo(todo: Post, current_user: Annotated[User, Depends(get_current_user)], conn= Depends(get_db)):
    if not todo:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    try:
        return await create_post(conn=conn, data=todo)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.put("/todos/{todo_id}", status_code=status.HTTP_200_OK)
async def update_todo(todo_id: int, todo: Post, current_user: Annotated[User, Depends(get_current_user)], conn= Depends(get_db)):
    try:
        return await update_post(conn=conn, id=todo_id, data=todo)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: int, current_user: Annotated[User, Depends(get_current_user)], conn= Depends(get_db)):
    try:
        return await delete_post(conn=conn, id=todo_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))