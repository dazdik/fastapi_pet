from dataclasses import dataclass
from datetime import date
from fastapi import Depends, FastAPI, Query
from pydantic import BaseModel
from typing import Optional

from app.bookings.router import router as router_bookings
from app.hotels.router import router as router_hotels
from app.users.router import router as router_users


app = FastAPI()


app.include_router(router_users)
app.include_router(router_bookings)
app.include_router(router_hotels)


class SHotel(BaseModel):
    addres: str
    name: str
    stars: int


@dataclass
class HotelSearchArgs:
    location: str
    date_from: date
    date_to: date
    has_spa: Optional[bool] = None
    stars: Optional[int] = Query(None, ge=1, le=5)


# @app.get('/hotels', response_model=list[SHotel])
# def get_hotels(search_args: HotelSearchArgs = Depends()
#                ):

#     return search_args
