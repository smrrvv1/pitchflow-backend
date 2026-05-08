from fastapi import FastAPI

from src.database import Base, engine
from src.models import User, Startup, Connection

from src.routers.users import router as users_router
from src.routers.startups import router as startups_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users_router)
app.include_router(startups_router)

@app.get("/")
def home():
    return {"message": "PitchFlow API works"}