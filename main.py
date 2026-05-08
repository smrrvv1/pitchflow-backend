from fastapi import FastAPI

from src.database import Base, engine
from src.models import User, Startup, Connection

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "PitchFlow API works"}