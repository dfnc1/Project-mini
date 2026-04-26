from typing import List

import asyncpg

from app.schemas import Post

async def add_post(data: Post, conn: asyncpg.Pool) -> Post:
    return await conn.fetchrow("INSERT INTO post (description, categories, amount) VALUES ($1, $2, $3)",
                               data.description, data.category, data.amount)

async def delete_post(id: int, conn: asyncpg.Pool) -> Post:
    return await conn.fetchrow("DELETE FROM post WHERE id = $1", id)

async def update_post(id: int, data: Post, conn: asyncpg.Pool) -> Post:
    return await conn.fetchrow("UPDATE post SET description = $1, categories = $2, amount = $3 WHERE id = $4",
                               data.description, data.category, data.amount, id)

async def get_posts(conn: asyncpg.Pool) -> List[Post]:
    return await conn.fetch("SELECT * FROM post ORDER BY id DESC")