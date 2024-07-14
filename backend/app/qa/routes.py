from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from auth import schemas as auth_schemas  # Importing User schema from auth.schemas
from qa import models, schemas
from database import get_db
from auth.routes import get_current_user

router = APIRouter()

@router.post("/questions/", response_model=schemas.Question)
def create_question(question: schemas.QuestionCreate, db: Session = Depends(get_db), current_user: auth_schemas.User = Depends(get_current_user)):
    db_question = models.Question(**question.dict(), owner_id=current_user.id)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

@router.post("/answers/", response_model=schemas.Answer)
def create_answer(answer: schemas.AnswerCreate, db: Session = Depends(get_db), current_user: auth_schemas.User = Depends(get_current_user)):
    db_answer = models.Answer(**answer.dict(), owner_id=current_user.id)
    db.add(db_answer)
    db.commit()
    db.refresh(db_answer)
    return db_answer
