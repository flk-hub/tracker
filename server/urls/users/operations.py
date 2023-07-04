"""Operations Module."""
from bcrypt import hashpw
from sqlalchemy.orm import Session

from ...databases.system import UserModel
from .types import UserCreate


def get_user(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.user_id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(UserModel).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    hashed_pass = hashpw(user.password.encode("utf-8"), user.email)
    new_user = UserModel(
        email=user.email, user_name=user.user_name, hashed_passwd=hashed_pass
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
