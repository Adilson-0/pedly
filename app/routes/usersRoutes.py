from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.schemas.userSchema import UserSchema
from app.models.userModel import User
from app.database import getSession

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.post("/reg")
async def regUser(body : UserSchema, session : Session = Depends(getSession)) -> User:
    user = User.userModelToSchema(body)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user