from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from app.database import get_db
from models.quiz_session import QuizSession
from services.quiz_service import calcular_puntuacion

router = APIRouter(prefix="/quiz-sessions", tags=["Quiz Sessions"])

@router.post("/")
def iniciar_sesion(db: Session = Depends(get_db)):
    session = QuizSession()
    db.add(session)
    db.commit()
    db.refresh(session)
    return session

@router.put("/{session_id}/complete")
def finalizar_sesion(session_id: int, db: Session = Depends(get_db)):
    session = db.query(QuizSession).get(session_id)
    session.estado = "completado"
    session.fecha_fin = datetime.utcnow()
    session.puntuacion_total = calcular_puntuacion(session.preguntas_correctas)
    db.commit()
    return session
