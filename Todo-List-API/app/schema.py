from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    password: str

class Post(BaseModel):
    title: str
    description: str