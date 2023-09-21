import asyncio
from datetime import date, datetime
from typing import List
from fastapi import APIRouter, Query

from app.hotels.schemas import SHotelIndividual, SHotelInfo
from app.hotels.dao import HotelDAO
from app.hotels.rooms.router import router as router_rooms


router = APIRouter(prefix='/hotels', tags=['Отели'])
router.include_router(router_rooms)

@router.get('/{location}')
async def get_hotels_loc_date(location: str,
                              date_from: date = Query(...,description=f'Пример: Дата заезда {datetime.now().date()}'),
                              date_to: date = Query(..., description=f'Пример: Дата выселения {datetime.now().date()}')
                              ) -> List[SHotelInfo]:
    await asyncio.sleep(3)
    hotels = await HotelDAO.find_location(location, date_from, date_to)
    return hotels


@router.get('/id/{hotel_id}')
async def get_hotel(hotel_id: int) -> SHotelIndividual:
    hotel = await HotelDAO.find_or_none(id=hotel_id)
    return hotel
