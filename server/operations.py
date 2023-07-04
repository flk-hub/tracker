"""Operations Module."""
from bcrypt import hashpw, gensalt
from sqlalchemy.orm import Session

from .models import TransactionModel, UserModel
from .schemas import TransactionCreate, UserCreate


def get_user(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.user_id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(UserModel).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    hashed_pwd = hashpw(user.password.encode("utf-8"), gensalt())
    new_user = UserModel(
        email=user.email, user_name=user.user_name, hashed_pwd=hashed_pwd
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_transactions(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return (
        db.query(TransactionModel)
        .filter(TransactionModel.issuer_id == user_id)
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_user_transaction(db: Session, transaction: TransactionCreate, user_id: int):
    db_item = TransactionModel(**transaction.dict(), issuer_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
