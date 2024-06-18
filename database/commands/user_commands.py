from typing import Set, Sequence, Union

from sqlalchemy import select, Select, Update, update

from services.logging_module import logger

from sqlalchemy.exc import IntegrityError, NoResultFound

from database.database import create_session
from database.models.models import User, Contact
from config.config import load_config, Config

config: Config = load_config()


class UserAPI:
    @staticmethod
    async def add_user() -> User:
        async with create_session() as session:
            user_object: User = User()
            session.add(user_object)
            try:
                await session.commit()
                await session.refresh(user_object)
                logger.info(f"Added user with id: {user_object.id}")
                return user_object
            except IntegrityError as error:
                logger.error(f"Error in function '{__name__}': {error}")
                await session.rollback()

    @staticmethod
    async def get_user(user_id: int) -> Union[Sequence[User], None]:
        async with create_session() as session:
            request: Select = select(User).where(User.id == user_id)
            try:
                return await session.execute(request).first()
            except NoResultFound as error:
                logger.error(f"Error in function '{__name__}': {error}")
                session.rollback()

    @staticmethod
    async def get_contacts(user_id: int) -> Union[Sequence[Set[Contact]], None]:
        async with create_session() as session:
            request: Select = select(User).where(User.id == user_id)
            try:
                return await session.execute(request).first().contacts
            except NoResultFound as error:
                logger.error(f"Error in function '{__name__}': {error}")
                session.rollback()
