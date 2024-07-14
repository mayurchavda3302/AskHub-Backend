from pydantic import BaseModel
from typing import List

class AnswerBase(BaseModel):
    body: str

class AnswerCreate(AnswerBase):
    question_id: int

class Answer(AnswerBase):
    id: int
    owner_id: int
    question_id: int

    class Config:
        from_attributes = True  # Use this instead of orm_mode for Pydantic v2

class QuestionBase(BaseModel):
    title: str
    body: str

class QuestionCreate(QuestionBase):
    pass

class Question(QuestionBase):
    id: int
    owner_id: int
    answers: List[Answer] = []

    class Config:
        from_attributes = True  # Use this instead of orm_mode for Pydantic v2
