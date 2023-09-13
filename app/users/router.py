from fastapi import APIRouter, Depends, Response, status
from app.users.dao import UsersDAO
from app.users.auth import authenticate, create_access_token, get_password_hash

from app.users.dependencies import get_current_user
from app.users.schemas import SUserAuth
from app.users.models import Users
from app.exceptions import InvalidAuthCException, UserAlreadyExistsException


router = APIRouter(prefix='/auth', tags=['Auth'])


@router.post('/register')
async def register_user(user_data: SUserAuth):
    is_user_exists = await UsersDAO.find_or_none(email=user_data.email)
    if is_user_exists:
        raise UserAlreadyExistsException
    hasshed_password = get_password_hash(user_data.password)
    await UsersDAO.add(email=user_data.email, hashed_password=hasshed_password)
    return status.HTTP_201_CREATED


@router.post('/login')
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticate(user_data.email, user_data.password)
    if not user:
        raise InvalidAuthCException
    access_token = create_access_token({'sub': str(user.id)})
    response.set_cookie('booking_access_token', access_token, httponly=True)
    return access_token


@router.post('/logout')
async def logout_user(response: Response):
    response.delete_cookie('booking_access_token')


@router.get('/me')
async def get_current_user(cur_user: Users = Depends(get_current_user)):
    return cur_user
