from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.question import Question
from app.models.quiz_session import QuizSession

router = APIRouter(prefix="/statistics", tags=["Statistics"])

@router.get("/global")
def estadisticas_globales(db: Session = Depends(get_db)):
    total_preguntas = db.query(Question).count()
    sesiones = db.query(QuizSession).count()
    return {
        "total_preguntas": total_preguntas,
        "total_sesiones": sesiones
    }
