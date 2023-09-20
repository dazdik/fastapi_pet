from typing import Optional
from pydantic import BaseModel


class SHotelInfo(BaseModel):
    id: int
    name: str
    location: str
    services: Optional[list[str]]
    room_quantity: int
    image_id: int
    rooms_left: int


class SHotelIndividual(BaseModel):
    id: int
    name: str
    location: str
    services: Optional[list[str]]
    room_quantity: int
    image_id: int
