from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models import Startup
from src.schemas import StartupCreate, StartupUpdate

router = APIRouter(
    prefix="/startups",
    tags=["Startups"]
)


@router.post("/")
def create_startup(startup: StartupCreate, db: Session = Depends(get_db)):
    new_startup = Startup(
        title=startup.title,
        one_liner=startup.one_liner,
        description=startup.description,
        tags=startup.tags,
        stage=startup.stage,
        target_amount=startup.target_amount,
        owner_id=startup.owner_id
    )

    db.add(new_startup)

    db.commit()

    db.refresh(new_startup)

    return new_startup


@router.get("/")
def get_startups(db: Session = Depends(get_db)):
    startups = db.query(Startup).all()

    return startups


@router.get("/{startup_id}")
def get_startup(startup_id: int, db: Session = Depends(get_db)):
    startup = db.query(Startup).filter(Startup.id == startup_id).first()

    if not startup:
        return {"message": "startup not found"}

    return startup


@router.delete("/{startup_id}")
def delete_startup(startup_id: int, db: Session = Depends(get_db)):
    startup = db.query(Startup).filter(
        Startup.id == startup_id
    ).first()

    if not startup:
        return {"message": "startup not found"}

    db.delete(startup)

    db.commit()

    return {"message": "startup deleted"}


@router.get("/my_startups/{user_id}")
def get_my_startups(user_id: int, db: Session = Depends(get_db)):
    startups = db.query(Startup).filter(
        Startup.owner_id == user_id
    ).all()

    return startups


@router.put("/{startup_id}")
def update_startup(
    startup_id: int,
    updated_startup: StartupUpdate,
    db: Session = Depends(get_db)
):
    startup = db.query(Startup).filter(
        Startup.id == startup_id
    ).first()

    if not startup:
        return {"message": "startup not found"}

    startup.title = updated_startup.title
    startup.one_liner = updated_startup.one_liner
    startup.description = updated_startup.description
    startup.tags = updated_startup.tags
    startup.stage = updated_startup.stage
    startup.target_amount = updated_startup.target_amount

    db.commit()

    db.refresh(startup)

    return startup