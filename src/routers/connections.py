from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models import Connection
from src.schemas import ConnectionCreate

router = APIRouter(
    prefix="/connections",
    tags=["Connections"]
)


@router.post("/")
def create_connection(
    connection: ConnectionCreate,
    db: Session = Depends(get_db)
):
    new_connection = Connection(
        startup_id=connection.startup_id,
        investor_id=connection.investor_id
    )

    db.add(new_connection)

    db.commit()

    db.refresh(new_connection)

    return new_connection


@router.get("/")
def get_connections(db: Session = Depends(get_db)):
    connections = db.query(Connection).all()

    return connections