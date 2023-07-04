"""Types Module."""
from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    user_name: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    user_id: int
    is_active: bool
    email: str

    class Config:
        orm_mode = True
