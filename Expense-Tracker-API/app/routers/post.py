from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from app.databases import get_db
from app.security import get_current_user
from app.schemas import User, Post
from app.repository.posts import add_post, delete_post, update_post, get_posts

router = APIRouter(prefix="/post", tags=["post"])

@router.post("/expense", status_code=status.HTTP_201_CREATED)
async def create_expense(data: Post, current_user: Annotated[User, Depends(get_current_user)], conn= Depends(get_db)):
    return await add_post(data= data, conn= conn)

@router.delete("/expense/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_expense(id: int, current_user: Annotated[User, Depends(get_current_user)], conn= Depends(get_db)):
    return await delete_post(id= id, conn= conn)

@router.patch("/expense/{id}", status_code=status.HTTP_200_OK)
async def update_expense(id: int, data: Post, current_user: Annotated[User, Depends(get_current_user)], conn= Depends(get_db)):
    return await update_post(id= id, data= data, conn= conn)

@router.get("/expense/", status_code=status.HTTP_200_OK)
async def get_expense(filter: str, current_user: Annotated[User, Depends(get_current_user)],conn= Depends(get_db)):
    return await get_expense(filter= filter, conn= conn)