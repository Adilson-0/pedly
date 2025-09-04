from fastapi import FastAPI
from .database import create_db_and_tables
from .routes import usersRoutes

app = FastAPI(title="Pedly API - documentation")
app.include_router(usersRoutes.router)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def hello():
    return {"msg":"Hello, world!"}
