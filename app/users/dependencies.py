from datetime import datetime
import jwt

from fastapi import Depends, Request

from app.config import settings
from app.users.dao import UsersDAO
from app.exceptions import InvalidAuthCException


def get_token(request: Request):
    token = request.cookies.get('booking_access_token')
    if not token:
        raise InvalidAuthCException
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload: dict = jwt.decode(token,
                                   settings.SECRET, settings.ALGORITHM)
    except jwt.InvalidTokenError:
        raise InvalidAuthCException
    expire: str = payload.get('exp')
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise InvalidAuthCException
    user_id: str = payload.get('sub')
    if not user_id:
        raise InvalidAuthCException
    user = await UsersDAO.find_by_id(int(user_id))
    if not user:
        raise InvalidAuthCException
    return user
