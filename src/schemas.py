from pydantic import BaseModel, field_validator


class UserCreate(BaseModel):
    full_name: str
    email: str
    password: str
    role: str

    @field_validator("full_name")
    @classmethod
    def validate_full_name(cls, value):
        if not value.replace(" ", "").isalpha():
            raise ValueError("full name should contain only letters")

        return value

    @field_validator("role")
    @classmethod
    def validate_role(cls, value):
        if value not in ["founder", "investor"]:
            raise ValueError("role should be founder or investor")

        return value


class StartupCreate(BaseModel):
    title: str
    one_liner: str
    description: str
    tags: str
    stage: str
    target_amount: str
    owner_id: int

    @field_validator("target_amount")
    @classmethod
    def validate_target_amount(cls, value):
        if not value.isdigit():
            raise ValueError("target amount should contain only numbers")

        return value

    @field_validator("stage")
    @classmethod
    def validate_stage(cls, value):
        if value not in ["idea", "mvp", "seed"]:
            raise ValueError("stage should be idea, mvp or seed")

        return value


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

    @field_validator("target_amount")
    @classmethod
    def validate_target_amount(cls, value):
        if not value.isdigit():
            raise ValueError("target amount should contain only numbers")

        return value

    @field_validator("stage")
    @classmethod
    def validate_stage(cls, value):
        if value not in ["idea", "mvp", "seed"]:
            raise ValueError("stage should be idea, mvp or seed")

        return value


class LoginSchema(BaseModel):
    email: str
    password: str