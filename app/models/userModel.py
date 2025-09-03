from __future__ import annotations
from sqlmodel import Field, SQLModel, Relationship
from typing import List, Optional

class User(SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(nullable=False, max_length=100, index=True)
    password: str = Field(nullable=False)
    email: str = Field(nullable=False)
    complete_name : str = Field(nullable=False)
    phone : Optional[str] = Field(default=None, nullable=True)

    products : List["Product"] = Relationship(back_populates="owner_product", cascade_delete=True)
    orders: List["Order"] = Relationship(back_populates="owner_order", cascade_delete=True)
    clients : List["Client"] = Relationship(back_populates="owner_client", cascade_delete=True)
