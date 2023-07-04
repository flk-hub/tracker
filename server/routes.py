"""Users service Routes Module."""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .models import get_db
from .schemas import Transaction, TransactionCreate, User, UserCreate
from . import operations

Router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@Router.post("/", response_model=User)
def create_users(user: UserCreate, db: Session = Depends(get_db)):
    db_user = operations.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return operations.create_user(db=db, user=user)


@Router.get("/", response_model=list[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = operations.get_users(db, skip=skip, limit=limit)
    return users


@Router.get("/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = operations.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@Router.post("/{user_id}/transactions/", response_model=Transaction)
def create_transaction_for_user(
    user_id: int, transaction: TransactionCreate, db: Session = Depends(get_db)
):
    return operations.create_user_transaction(
        db=db, transaction=transaction, user_id=user_id
    )


@Router.get("/{user_id}/transactions/", response_model=List[Transaction])
def read_transactions(
    user_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    return operations.get_user_transactions(db, user_id=user_id, skip=skip, limit=limit)
