import asyncpg

from app.schemas import UserInDB, User

async def add_user(payload: UserInDB, conn: asyncpg.Pool) -> User:
    return await conn.fetchrow("INSERT INTO users (username, email, hashed_password) VALUES ($1, $2) RETURNING username",
                               user.username, user.email, user.hashed_password)

async def get_user(email: str, conn: asyncpg.Pool) -> User:
    return await conn.fetchrow("SELECT * FROM users WHERE email = $1", email)