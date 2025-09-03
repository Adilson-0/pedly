from __future__ import annotations
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from .orderProductLinkModel import OrderProductLink

class Product(SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    name : str = Field(nullable=False, max_length=100, index=True)
    price : float

    user_id : Optional[int] = Field(foreign_key="user.id")

    owner_product : Optional["User"] = Relationship(back_populates="products")
    orders : List["Order"] = Relationship(back_populates="products", link_model=OrderProductLink)
