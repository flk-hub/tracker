"""Schemas Module."""
from datetime import datetime
from pydantic import BaseModel, Field


class TransactionBase(BaseModel):
    value: float
    category: str
    description: str
    date: datetime = Field(default_factory=datetime.now)
    in_out: bool = False


class TransactionCreate(TransactionBase):
    pass


class Transaction(TransactionBase):
    transaction_id: int
    issuer_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str
    user_name: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    user_id: int
    is_active: bool
    email: str
    transactions: list[Transaction] = []

    class Config:
        orm_mode = True
