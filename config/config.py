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


def load_config(path: Union[str | None] = None):
    env = Env()
    env.read_env(path)
    return Config(TelegramBotToken=BotToken(env("BOT_TOKEN")),
                  DataBase=PostgreSQL(USER=env("POSTGRES_USER"),
                                      PASSWORD=env("POSTGRES_PASSWORD"),
                                      HOST=env("POSTGRES_HOST"),
                                      PORT=env("POSTGRES_PORT"),
                                      NAME=env("POSTGRES_DB")))
