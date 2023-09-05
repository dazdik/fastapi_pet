from fastapi import APIRouter

from app.bookings.dao import BookigDAO
from app.bookings.schemas import SBooking


router = APIRouter(
    prefix='/bookings',
    tags=['Брони']
)


@router.get('/')
async def get_bookings() -> list[SBooking]:
    return await BookigDAO.get_find_all()
