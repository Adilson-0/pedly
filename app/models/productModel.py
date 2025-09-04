from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING
from .orderProductLinkModel import OrderProductLink

if(TYPE_CHECKING):
    from .userModel import User
    from .orderModel import Order

class Product(SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    name : str = Field(nullable=False, max_length=100, index=True)
    price : float

    user_id : Optional[int] = Field(foreign_key="user.id")

    owner_product : "User" = Relationship(back_populates="products")
    orders : List["Order"] = Relationship(back_populates="products", link_model=OrderProductLink)

# COLOCA A PORRA DOS IMPORTS DIREITO, ESQUECE O QUE O CHAT GEPETO FALOU