"""System Database Module."""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import sessionmaker

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
    email = Column(String, unique=True, index=True)
    hashed_pwd = Column(String)
    user_name = Column(String)
    is_active = Column(Boolean, default=True)
