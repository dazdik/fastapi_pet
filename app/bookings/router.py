from fastapi import APIRouter, Depends, Request

from app.bookings.dao import BookigDAO
from app.bookings.schemas import SBooking
from app.users.dependencies import get_current_user
from app.users.models import Users


router = APIRouter(
    prefix='/bookings',
    tags=['Брони']
)


@router.get('/')
async def get_bookings(user: Users = Depends(get_current_user)):
    return await BookigDAO.get_find_all(user_id=user.id)
