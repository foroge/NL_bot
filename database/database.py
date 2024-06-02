from contextlib import asynccontextmanager

from typing import AsyncGenerator

from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from config import Config
from services.logging import logger


class Base(DeclarativeBase):
    pass


config: Config = load_config()

url = URL.create(
    drivername="postgresql+asyncpg",
    username=config.DataBase.USER,
    password=config.DataBase.PASSWORD,
    host=config.DataBase.HOST,
    port=config.DataBase.PORT,
    database=config.DataBase.NAME
)
engine: AsyncEngine = create_async_engine(url=url)


async def create_base() -> None:
    async with engine.begin() as connection:
        logger.debag("Creating tables in the DB")
        await connection.run_sync(Base.meta.create_all)
        logger.debag("Success of creating tables in the DB")


@asynccontextmanager
async def create_session() -> AsyncGenerator[AsyncSession, None]:
    try:
        async with async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False) as session:
            yield session
    except Exception as error:
        await session.rollback()
        logger.error(f"Indentation error in function '{__name__}': {error}")
        raise
    finally:
        logger.debug("Closed session!")
        await session.close()
