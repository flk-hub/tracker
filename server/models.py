"""System Database Module."""
from datetime import datetime
from sqlalchemy import DateTime, Float, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import sessionmaker, relationship

_DATABASE_URL = "sqlite:///test.db"

_ENGINE = create_engine(_DATABASE_URL, connect_args={"check_same_thread": False})
DB_SESSION = sessionmaker(autocommit=False, autoflush=False, bind=_ENGINE)

DatabaseModel = declarative_base()


# Dependency
def get_db():
    """Get the database."""
    db = DB_SESSION()
    try:
        yield db
    finally:
        db.close()


def create_db():
    """Create a new database."""
    DatabaseModel.metadata.create_all(bind=_ENGINE)


class UserModel(DatabaseModel):
    """Users table Model."""

    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String(50), unique=True, index=True)
    hashed_pwd = Column(String)
    user_name = Column(String(20))
    is_active = Column(Boolean, default=True)
    transactions = relationship("TransactionModel", back_populates="issuer")


class TransactionModel(DatabaseModel):
    __tablename__ = "transactions"

    transaction_id = Column(Integer, primary_key=True, index=True)
    value = Column(Float, default=0)
    category = Column(String(40))
    description = Column(String)
    in_out = Column(Boolean, default=False)  # false == in
    date = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    issuer_id = Column(Integer, ForeignKey("users.user_id"))
    issuer = relationship("UserModel", back_populates="transactions")
