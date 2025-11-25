from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from . import Base # Import Base from the same directory

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    answer = Column(String, nullable=False)
    language = Column(String, default="english")
    subject = Column(String, nullable=False)
    class_level = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    owner_id = Column(Integer, ForeignKey("users.id"))

    # This creates a relationship to the User model
    owner = relationship("User", backref="questions")