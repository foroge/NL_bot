from typing import Union
from dataclasses import dataclass

from environs import Env


@dataclass
class BotToken:
    TOKEN: str


@dataclass
class PostgreSQL:
    USER: str
    PASSWORD: str
    HOST: str
    PORT: int
    NAME: str


@dataclass
class Config:
    TelegramBotToken: BotToken
    DataBase: PostgreSQL


def load_config(path: Union[str | None] = None, test: bool = False):
    env = Env()
    env.read_env(path)
    name: str = env("POSTGRES_DB") if not test else env("POSTGRES_TEST_DB")
    return Config(TelegramBotToken=BotToken(env("BOT_TOKEN")),
                  DataBase=PostgreSQL(USER=env("POSTGRES_USER"),
                                      PASSWORD=env("POSTGRES_PASSWORD"),
                                      HOST=env("POSTGRES_HOST"),
                                      PORT=env("POSTGRES_PORT"),
                                      NAME=name))
