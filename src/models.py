from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    email = Column(String)
    password = Column(String)
    role = Column(String)

    startups = relationship("Startup", back_populates="owner")


class Startup(Base):
    __tablename__ = "startups"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    one_liner = Column(String)
    description = Column(String)
    tags = Column(String)
    stage = Column(String)
    target_amount = Column(String)

    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="startups")


class Connection(Base):
    __tablename__ = "connections"

    id = Column(Integer, primary_key=True)

    startup_id = Column(Integer, ForeignKey("startups.id"))
    investor_id = Column(Integer, ForeignKey("users.id"))