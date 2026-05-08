from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models import User
from src.schemas import UserCreate

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(
        full_name=user.full_name,
        email=user.email,
        password=user.password,
        role=user.role
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return new_user


@router.get("/")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()

    return users


@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    return user