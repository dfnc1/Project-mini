import asyncpg
from sqlalchemy.sql.functions import user

from app.schemas import UserInDB, User

async def add_user(user: UserInDB, conn: asyncpg.Pool) -> User:
    return await conn.fetchrow("INSERT INTO users (username, hashed_password) VALUES ($1, $2)",
                               user.username, user.hashed_password)

async def get_user(conn: asyncpg.Pool) -> User:
    return await conn.fetchrow("SELECT * FROM users WHERE username = $1",
                               user.username)