import enum
import datetime
from typing import Annotated, List, Optional

from sqlalchemy import ForeignKey, text, BigInteger, event
from sqlalchemy.orm import mapped_column, Mapped, relationship

from database.database import Base

PRIM_ID = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]


class User(Base):
    __tablename__ = 'users'

    id: PRIM_ID
    contacts: Mapped[Set["Contact"]] = relationship("user")


class Contact(Base):
    __tablename__ = "contacts"

    id: PRIM_ID
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship("contacts")
    products: Mapped[Set["Product"]] = relationship("contact")
    characteristics: Mapped[Set["Characteristic"]] = relationship("contact")


class Product(Base):
    __tablename__ = "products"

    id: PRIM_ID

    title: Mapped[str]
    task: Mapped[str]
    quantity: Mapped[str]
    date_of_use: Mapped[datetime.date]
    note: Mapped[str]

    contact_id: Mapped[int] = mapped_column(ForeignKey("contacts.id"))
    contact: Mapped["Contact"] = relationship("products")


class Characteristic(Base):
    __tablename__ = "characteristics"

    id: PRIM_ID

    title: Mapped[str]
    description: Mapped[str]
    type: Mapped[str]

    contact_id: Mapped[int] = mapped_column(ForeignKey("contacts.id"))
    contact: Mapped["Contact"] = relationship("characteristics")
