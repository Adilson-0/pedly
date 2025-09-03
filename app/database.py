from sqlmodel import Session, create_engine, SQLModel
from os import environ
from .models import clientModel, userModel, productModel, orderProductLinkModel, orderModel

DATABASE_URL = f"postgresql+psycopg2://pedlyadm:{environ['pedlyUserDBPassword']}@localhost:5432/pedlyProject"

engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine, checkfirst=True)

def getSession():
    with Session(engine) as session:
        yield session