from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..utils.config import settings

# 1. Create the Base class for our models to inherit from
Base = declarative_base()

# 2. Create the SQLAlchemy engine
engine = create_engine(settings.DATABASE_URL)

# 3. Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Dependency to get a DB session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 5. Import and re-export the models so they are available when importing from 'app.models'
from .user import User
from .question import Question

# Define what __all__ exports
__all__ = ["Base", "engine", "SessionLocal", "get_db", "User", "Question"]