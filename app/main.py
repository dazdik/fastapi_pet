from dataclasses import dataclass
from datetime import date
from fastapi import Depends, FastAPI, Query
from pydantic import BaseModel
from typing import Optional

from app.bookings.router import router as router_bookings


app = FastAPI()

app.include_router(router_bookings)

class SHotel(BaseModel):
    addres: str
    name: str
    stars: int


@dataclass
class HotelSerachArgs:
    location: str
    date_from: date
    date_to: date
    has_spa: Optional[bool] = None
    stars: Optional[int] = Query(None, ge=1, le=5)


@app.get('/hotels', response_model=list[SHotel])
def get_hotels(searcj_args: HotelSerachArgs = Depends()
               ):

    return searcj_args


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post('/bookings')
def add_booking(booking: SBooking):
    pass
