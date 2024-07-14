# qa/models.py
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from database import Base
from auth.models import User

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(Text, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="questions")

class Answer(Base):
    __tablename__ = "answers"
    id = Column(Integer, primary_key=True, index=True)
    body = Column(Text, nullable=False)
    question_id = Column(Integer, ForeignKey("questions.id"))
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="answers")
    question = relationship("Question", back_populates="answers")

User.questions = relationship("Question", back_populates="owner")
User.answers = relationship("Answer", back_populates="owner")
Question.answers = relationship("Answer", back_populates="question")
