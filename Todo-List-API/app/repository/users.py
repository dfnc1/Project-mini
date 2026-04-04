from fastapi import HTTPException


async def get_user(email: str, conn):
    try:
        user = await conn.fetchrow("SELECT * FROM users where email = $1", email)
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

