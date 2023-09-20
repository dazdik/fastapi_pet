from fastapi import HTTPException, status


class BookingsExceptions(HTTPException):
    status_code = 500
    detail = ''

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class InvalidAuthCException(BookingsExceptions):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Не хватает действительных учётных данных'


class UserAlreadyExistsException(BookingsExceptions):
    status_code = status.HTTP_409_CONFLICT
    detail = 'Пользователь уже существует'


class RoomAlreadyReservedException(BookingsExceptions):
    status_code = status.HTTP_409_CONFLICT
    detail = 'Все номера заняты'
