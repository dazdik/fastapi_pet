from pydantic import BaseModel
# from typing import Optional


class SRoom(BaseModel):
    id: int
    hotel_id: int
    name: str
    description: str
    services: list[str]
    price: int
    quantity: int
    image_id: int
    rooms_left: int
