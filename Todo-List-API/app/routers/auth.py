from typing import Annotated
from datetime import timedelta

from pwdlib import PasswordHash
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from .. import Register, get_db, get_user_by_email, authenticate_user, create_access_token, Token
router = APIRouter(prefix="/auth", tags=["auth"], responses={404: {"description": "Not found"}})
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

password_hasher = PasswordHash.recommended()
ACCESS_TOKEN_EXPIRE_MINUTES = 30

@router.post("/register")
async def register(payload: Register, conn= Depends(get_db)):
    if not payload:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    exist_user = await get_user_by_email(payload.email, conn)
    if exist_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    try:
        await conn.fetchrow("INSERT INTO users (NAME, EMAIL, PASSWORD) VALUES ($1, $2, $3)",
                            payload.username, payload.email, password_hasher.hash(payload.password))
        access_token = create_access_token(
            data={"sub": payload.username}, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
        return Token(access_token=access_token, token_type="bearer")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.post("/login")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], conn= Depends(get_db)):
    user = await authenticate_user(form_data.username, form_data.password, conn)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    access_token = create_access_token(
        data={"sub": user["name"]}, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return Token(access_token=access_token, token_type="bearer")