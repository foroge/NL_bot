import enum
import datetime
from typing import Annotated, List, Optional, Set

from sqlalchemy import ForeignKey, text, BigInteger, event
from sqlalchemy.orm import mapped_column, Mapped, relationship

from database.database import Base

PRIM_ID = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]


class User(Base):
    __tablename__ = 'users'

    id: Mapped[PRIM_ID]
    contacts: Mapped[Set["Contact"]] = relationship(back_populates="user")


class Contact(Base):
    __tablename__ = "contacts"

    id: Mapped[PRIM_ID]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="contacts")
    products: Mapped[Set["Product"]] = relationship(back_populates="contact")
    characteristics: Mapped[Set["Characteristic"]] = relationship(back_populates="contact")


class Product(Base):
    __tablename__ = "products"

    id: Mapped[PRIM_ID]

    title: Mapped[str]
    task: Mapped[str]
    quantity: Mapped[str]
    date_of_use: Mapped[datetime.date]
    note: Mapped[str]

    contact_id: Mapped[int] = mapped_column(ForeignKey("contacts.id"))
    contact: Mapped["Contact"] = relationship(back_populates="products")


class Characteristic(Base):
    __tablename__ = "characteristics"

    id: Mapped[PRIM_ID]

    title: Mapped[str]
    description: Mapped[str]
    type: Mapped[str]

    contact_id: Mapped[int] = mapped_column(ForeignKey("contacts.id"))
    contact: Mapped["Contact"] = relationship(back_populates="characteristics")

