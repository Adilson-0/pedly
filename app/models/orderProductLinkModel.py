from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

class OrderProductLink(SQLModel, table=True):
    id_order : Optional[int] = Field(default=None, foreign_key="order.id", primary_key=True)
    id_product : Optional[int] = Field(default=None, foreign_key="product.id", primary_key=True)