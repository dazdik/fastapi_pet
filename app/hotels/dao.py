from datetime import date
from sqlalchemy import and_, func, or_, select
from app.dao.base import BaseDAO
from app.hotels.models import Hotels
from app.database import async_session_maker
from app.bookings.models import Bookings
from app.hotels.rooms.models import Rooms


class HotelDAO(BaseDAO):
    model = Hotels

    @classmethod
    async def find_location(cls, location: str,
                            date_from: date, date_to: date):
        async with async_session_maker() as session:
            query = (select(Bookings).filter(
                or_(and_(Bookings.date_from < date_from,
                         Bookings.date_to > date_from),
                    and_(Bookings.date_from >= date_from,
                         Bookings.date_from < date_to)),
                ).subquery('filter_rooms'))
            hotels_rooms_left = (select(
                (Hotels.room_quantity - func.count(query.c.room_id)).label(
                    'rooms_left'), Rooms.hotel_id).select_from(
                Hotels
                ).outerjoin(Rooms, Rooms.hotel_id == Hotels.id).outerjoin(
                    query, query.c.room_id == Rooms.id).where(
                        Hotels.location.contains(location.title())).group_by(
                            Hotels.room_quantity, Rooms.hotel_id
                        ).cte('hotels_rooms_left'))

            get_hotels_info = (select(Hotels.__table__.columns,
                                      hotels_rooms_left.c.rooms_left)
                               .select_from(Hotels).join(hotels_rooms_left,
                                                         hotels_rooms_left.c.hotel_id == Hotels.id)
                               .where(hotels_rooms_left.c.rooms_left > 0))
            hotels_info = await session.execute(get_hotels_info)
            return hotels_info.all()
