from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.repository.users import add_user
from app.schemas import Token, Register, UserInDB
from app.databases import get_db
from app.security import get_password_hash, create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/signup", response_model=Token)
async def signup(payload: Register, conn= Depends(get_db)):
    if not payload:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    try:
        new_user = UserInDB(name=payload.name, email=payload.email, hashed_password=get_password_hash(payload.password))
        await add_user(payload=new_user, conn=conn)

        access_token = create_access_token(data={"sub": payload.email})
        return Token(access_token=access_token, token_type="bearer")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.post("/login", response_model=Token)
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], conn= Depends(get_db)):
    user = None
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password", headers={"WWW-Authenticate": "Bearer"})
    pass