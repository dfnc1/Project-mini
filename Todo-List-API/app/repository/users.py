from fastapi import HTTPException


async def get_user(username: str, conn):
    try:
        user = await conn.fetchrow("SELECT * FROM users where name = $1", username)
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

async def get_user_by_email(email: str, conn):
    try:
        user = await conn.fetchrow("SELECT * FROM users where email = $1", email)
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

