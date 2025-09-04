from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING

if(TYPE_CHECKING):
    from .userModel import User

class Client(SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(nullable=False, max_length=100, index=True)
    cnpj: str = Field(nullable=False)
    address: Optional[str] = Field(default=None, nullable=True)
    phone: Optional[str] = Field(default=None, nullable=True)
    fantasy_name: Optional[str] = Field(default=None, nullable=True)

    user_id : Optional[int] = Field(default=None, foreign_key="user.id")

    owner_client : "User" = Relationship(back_populates="clients")