from datetime import date
from fastapi import APIRouter, Depends

from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking
from app.users.dependencies import get_current_user
from app.users.models import Users
from app.exceptions import RoomAlreadyReservedException


router = APIRouter(
    prefix='/bookings',
    tags=['Брони']
)


@router.get('/')
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBooking]:
    return await BookingDAO.get_find_all(user_id=user.id)


@router.post('/')
async def add_bookings(room_id: int, date_from: date, date_to: date,
                       user: Users = Depends(get_current_user)):
    booking = await BookingDAO.add(user.id, room_id, date_from, date_to)
    if not booking:
        raise RoomAlreadyReservedException


@router.delete('/{booking_id}', status_code=204)
async def delete_booking(booking_id: int,
                         user: Users = Depends(get_current_user)):
    return await BookingDAO.delete(booking_id, user.id)
