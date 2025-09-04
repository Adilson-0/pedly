from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING
from .orderProductLinkModel import OrderProductLink

if(TYPE_CHECKING):
    from .userModel import User
    from .productModel import Product

class Order(SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(default=None, index=True, foreign_key="user.id")
    
    owner_order : "User" = Relationship(back_populates="orders")
    products : List["Product"] = Relationship(back_populates="orders", link_model=OrderProductLink)
