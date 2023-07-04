"""Users service Routes Module."""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ...databases.system import get_db
from .operations import create_user, get_user, get_user_by_email, get_users
from .types import User, UserCreate

UsersRouter = APIRouter(
    prefix="/users",
    tags=["users"],
)


@UsersRouter.post("/", response_model=User)
def create_users(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)


@UsersRouter.get("/", response_model=list[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users


@UsersRouter.get("/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
