from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from models.question import Question
from schemas.question import QuestionCreate, QuestionResponse
import random

router = APIRouter(prefix="/questions", tags=["Questions"])

@router.post("/", response_model=QuestionResponse)
def crear_pregunta(data: QuestionCreate, db: Session = Depends(get_db)):
    q = Question(**data.model_dump())
    db.add(q)
    db.commit()
    db.refresh(q)
    return q

@router.get("/")
def listar_preguntas(db: Session = Depends(get_db)):
    return db.query(Question).filter(Question.is_active == True).all()

@router.get("/{question_id}", response_model=QuestionResponse)
def obtener_pregunta(question_id: int, db: Session = Depends(get_db)):
    q = db.query(Question).filter(Question.id == question_id).first()
    if not q:
        raise HTTPException(404, "Pregunta no encontrada")
    return q

@router.get("/random/")
def preguntas_random(limit: int = 5, db: Session = Depends(get_db)):
    preguntas = db.query(Question).filter(Question.is_active == True).all()
    return random.sample(preguntas, min(limit, len(preguntas)))
