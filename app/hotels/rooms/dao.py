from datetime import date
from sqlalchemy import and_, func, or_, select
from app.dao.base import BaseDAO
from app.hotels.models import Hotels
from app.database import async_session_maker
from app.bookings.models import Bookings
from app.hotels.rooms.models import Rooms


class RoomDAO(BaseDAO):
    model = Rooms

    @classmethod
    async def find_rooms(cls, hotel_id: int, date_from: date, date_to: date):
        async with async_session_maker() as session:
            query = (select(Bookings).filter(
                or_(and_(Bookings.date_from < date_from,
                         Bookings.date_to > date_from),
                    and_(Bookings.date_from >= date_from,
                         Bookings.date_from < date_to)),
                ).subquery('filter_rooms'))
            rooms_left = (select(
                (Rooms.quantity - func.count(query.c.room_id)).label(
                    'rooms_left'), Rooms.id.label('room_id')).select_from(
                Rooms
                ).outerjoin(
                    query, query.c.room_id == Rooms.id).where(
                        Rooms.hotel_id == hotel_id).group_by(
                            Rooms.quantity, query.c.room_id, Rooms.id
                        ).cte('rooms_left'))
            get_rooms_info = (select(Rooms.__table__.columns,
                                     rooms_left.c.rooms_left)
                              .select_from(Rooms).join(rooms_left,
                                                       rooms_left.c.room_id == Rooms.id)
                              .where(rooms_left.c.rooms_left > 0))
            rooms_info = await session.execute(get_rooms_info)
            return rooms_info.all()
