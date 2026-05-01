from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from app.databases import get_db
from app.security import get_current_user
from app.schemas import User, Post
from app.repository.posts import add_post, delete_post, update_post, get_posts

router = APIRouter(prefix="/post", tags=["post"])

@router.post("/expense", status_code=status.HTTP_201_CREATED)
async def create_expense(data: Post, current_user: Annotated[User, Depends(get_current_user)], conn= Depends(get_db)):
    try:
        return await add_post(data= data, conn= conn)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.delete("/expense/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_expense(id: int, current_user: Annotated[User, Depends(get_current_user)], conn= Depends(get_db)):
    try:
        return await delete_post(id= id, conn= conn)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.patch("/expense/{id}", status_code=status.HTTP_200_OK)
async def update_expense(id: int, data: Post, current_user: Annotated[User, Depends(get_current_user)], conn= Depends(get_db)):
    try:
        return await update_post(id= id, data= data, conn= conn)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/expense/", status_code=status.HTTP_200_OK)
async def get_expense(
        current_user: Annotated[User, Depends(get_current_user)],
        conn= Depends(get_db),
        filter_date: int | None = None,
        start_date: str | None = None,
        end_date: str | None = None
):
    try:
        return await get_posts(filter_date=filter_date ,start_date=start_date, end_date=end_date, conn= conn)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
