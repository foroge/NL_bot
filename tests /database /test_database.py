# from unittest import TestCase, defaultTestLoader, TextTestRunner, TestSuite

import asyncio

from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine

from config.config import Config, load_config
from services.logging_module import logger
from database.database import create_base, get_session
from database.models import User

# config: Config = load_config(test=True)
#
# url = URL.create(
#     drivername="postgresql+asyncpg",
#     username=config.DataBase.USER,
#     password=config.DataBase.PASSWORD,
#     host=config.DataBase.HOST,
#     port=config.DataBase.PORT,
#     database=config.DataBase.NAME
# )
# logger.debug(f"Url created: {url}")
# engine: AsyncEngine = create_async_engine(url=url)
#
#
# async def create_base() -> None:
#     async with engine.begin() as connection:
#         logger.debag("Creating tables in the DB")
#         await connection.run_sync(Base.meta.create_all)
#         logger.debag("Success of creating tables in the DB")
#
#
# @asynccontextmanager
# async def get_session() -> AsyncGenerator[AsyncSession, None]:
#     try:
#         global engine
#         async with async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)() as session:
#             yield session
#     except Exception as error:
#         await session.rollback()
#         logger.error(f"Indentation error in function '{__name__}': {error}")
#         raise
#     finally:
#         logger.debug("Closed session!")
#         await session.close()


async def test():
    await create_base()
    async with get_session() as session:
        user = User()
        session.add(user)
        try:
            await session.flush()
            await session.commit()
            logger.info("User added to DB")
        except IntegrityError as IE:
            logger.error(f"Indentation error in function '{__name__}': {IE}")
            await session.rollback()

    async with get_session() as session:
        print(await session.execute(select(User)))


asyncio.run(test())

# class TestUserDBCommand(TestCase):
#     class TestCreateUser(TestCase):
#         async def test_correct_data(self):
#             with get_session() as session:
#                 user = User()
#                 session.add(user)
#                 try:
#                     await session.flush()
#                     await session.commit()
#                     logger.info("User added to DB")
#                 except IntegrityError as IE:
#                     logger.error(f"Indentation error in function '{__name__}': {IE}")
#                     await session.rollback()
#
#
# class TestCreateUser:
#     pass
#
#
# async def test_all():
#     # suite_test_create_user = TestSuite(TestCreateUser)
#     ...
#
# if __name__ == "__main__":
#     test_all()
