import asyncpg

from app.schemas import UserInDB

async def get_user(email: str, conn: asyncpg.Pool):
    return await conn.fetchrow("SELECT * FROM users where email = $1", email)

async def add_user(new_data: UserInDB, conn: asyncpg.Pool):
    return await conn.fetchrow("INSERT INTO users (name, email, password) VALUES ($1, $2, $3)",
                            new_data.name, new_data.email, new_data.hashed_password)
