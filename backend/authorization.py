from firebase_admin import auth
from fastapi import Depends, HTTPException, status

async def get_user(token: str = Depends(auth.verify_id_token)):
    user = auth.get_user(token)

    if user:
        return user
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        ) 