from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str

class UserInDB(User):
    hashed_password: str

class Register(BaseModel):
    name: str
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str

class Post(BaseModel):
    title: str
    description: str