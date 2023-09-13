from datetime import datetime, timedelta

from pydantic import EmailStr
from app.config import settings
from app.users.dao import UsersDAO
import jwt
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hash_password: str) -> bool:
    return pwd_context.verify(plain_password, hash_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=1)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode,
                             settings.SECRET, settings.ALGORITHM)
    return encoded_jwt


async def authenticate(email: EmailStr, password: str) -> bool:
    user = await UsersDAO.find_or_none(email=email)
    if not user and not verify_password(password, user.password):
        return None
    return user
