from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import Integer, String, Float, Boolean


class Base(DeclarativeBase):
    pass


class Item(Base):
    __tablename__ = "items"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(50))
    price = mapped_column(Float)
    in_stock = mapped_column(Boolean, default=True)
