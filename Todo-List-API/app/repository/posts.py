import asyncpg

from app.schemas import Post

async def create_post(conn: asyncpg.Pool, todo: Post) :
    return await conn.fetchrow("INSERT INTO posts (title, description) VALUES ($1, $2) RETURNING id, title, description",
                               todo.title, todo.description)

async def update_post(conn: asyncpg.Pool, id: int, todo: Post):
    return await conn.fetchrow("UPDATE posts SET title = $1, description = $2 WHERE id=$3",
                               todo.title, todo.description, id)

async def delete_post(conn: asyncpg.Pool, id: int):
    return await conn.fetchrow("DELETE FROM posts WHERE id = $1",
                               id)

async def get_post(conn: asyncpg.Pool, id: int | None = None):
    if id is None:
        return await conn.fetchrow("SELECT * FROM posts")
    else:
        return await conn.fetchrow("SELECT * FROM posts WHERE id = $1",
                                   id)