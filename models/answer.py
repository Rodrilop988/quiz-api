from sqlalchemy import Column, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.database import Base

class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True, index=True)
    quiz_session_id = Column(Integer, ForeignKey("quiz_sessions.id"))
    question_id = Column(Integer, ForeignKey("questions.id"))
    respuesta_seleccionada = Column(Integer)
    es_correcta = Column(Boolean)
    tiempo_respuesta_segundos = Column(Integer, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
