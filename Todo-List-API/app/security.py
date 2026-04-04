from datetime import datetime, timedelta, timezone
from typing import Annotated
import os

from fastapi import Depends, HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv
from pwdlib import PasswordHash
import jwt
from jwt.exceptions import InvalidTokenError

from .schemas import TokenData
from .repository import get_user

load_dotenv()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
password_hash = PasswordHash.recommended()

def get_password_hash(password):
    return password_hash.hash(password)

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM"))
    return encoded_jwt

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], conn):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=[os.getenv("ALGORITHM")])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except InvalidTokenError:
        raise credentials_exception

    user = get_user(email= token_data.email, conn=conn)
    if user is None:
        raise credentials_exception
    return user

async def authenticate_user(email: str, password: str, conn):
    user = await get_user(email, conn)
    if not user:
        return False
    if not verify_password(password, user["password"]):
        return False
    return user