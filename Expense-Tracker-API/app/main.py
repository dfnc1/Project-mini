from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.databases import get_pool, close_pool
from app.routers import auth

@asynccontextmanager
async def lifespan(app: FastAPI):
    await get_pool()
    yield
    await close_pool()
app = FastAPI(lifespan=lifespan)

app.include_router(auth.router)