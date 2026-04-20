import asyncpg, os
from dotenv import load_dotenv

load_dotenv()
pool = None

async def get_pool():
    global pool
    pool = await asyncpg.create_pool(
        dsn=os.getenv("DATABASE_URL"),
        min_size=1,
        max_size=10
    )

async def close_pool():
    global pool
    await pool.close()

async def get_db():
    global pool
    async with pool.acquire() as conn:
        yield conn