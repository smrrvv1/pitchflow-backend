from pydantic import BaseModel


class UserCreate(BaseModel):
    full_name: str
    email: str
    password: str
    role: str


class StartupCreate(BaseModel):
    title: str
    one_liner: str
    description: str
    tags: str
    stage: str
    target_amount: str
    owner_id: int


class ConnectionCreate(BaseModel):
    startup_id: int
    investor_id: int


class StartupUpdate(BaseModel):
    title: str
    one_liner: str
    description: str
    tags: str
    stage: str
    target_amount: str


class LoginSchema(BaseModel):
    email: str
    password: str