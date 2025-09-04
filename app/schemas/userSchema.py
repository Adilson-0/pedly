from sqlmodel import SQLModel, Field
from typing import Optional

class UserSchema(SQLModel, table=False):
    username: str = Field(nullable=False, max_length=100, index=True)
    password: str = Field(nullable=False)
    email: str = Field(nullable=False)
    complete_name : str = Field(nullable=False)
    phone : Optional[str] = Field(default=None, nullable=True)