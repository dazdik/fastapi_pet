import asyncio
from datetime import date, datetime
from typing import List
from fastapi import APIRouter, Query

from app.hotels.rooms.schemas import SRoom
from app.hotels.rooms.dao import RoomDAO

router = APIRouter()


@router.get('/{hotel_id}/rooms')
async def get_rooms(hotel_id: int, date_from: date = Query(..., description=f'Пример: Дата заезда {datetime.now().date()}'),
                    date_to: date = Query(..., description=f'Пример: Дата выселения {datetime.now().date()}')
                    ) -> List[SRoom]:
    await asyncio.sleep(3)
    rooms = await RoomDAO.find_rooms(hotel_id, date_from, date_to)
    return rooms
