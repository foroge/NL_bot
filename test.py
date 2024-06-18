from contextlib import asynccontextmanager

from typing import AsyncGenerator

from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from config.config import Config, load_config
from services.logging_module import logger
from database.database import Base


config: Config = load_config(test=True)

url = URL.create(
    drivername="postgresql+asyncpg",
    username=config.DataBase.USER,
    password=config.DataBase.PASSWORD,
    host=config.DataBase.HOST,
    # port=config.DataBase.PORT,
    database=config.DataBase.NAME
)
print(url)
logger.debug(f"Url created: {url}")
engine = create_async_engine(url=url)
print(engine)

async def create_base() -> None:
    async with engine.begin() as connection:
        logger.debag("Creating tables in the DB")
        await connection.run_sync(Base.meta.create_all)
        logger.debag("Success of creating tables in the DB")


@asynccontextmanager
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    try:
        global engine
        async with async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)() as session:
            yield session
    except Exception as error:
        await session.rollback()
        logger.error(f"Indentation error in function '{__name__}': {error}")
        raise
    finally:
        logger.debug("Closed session!")
        await session.close()