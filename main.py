from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from src.database import Base, engine
from src.models import User, Startup, Connection

from src.routers.users import router as users_router
from src.routers.startups import router as startups_router
from src.routers.connections import router as connections_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router)
app.include_router(startups_router)
app.include_router(connections_router)

@app.get("/")
def home():
    return {"message": "PitchFlow API works"}