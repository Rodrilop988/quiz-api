from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.database import Base

class QuizSession(Base):
    __tablename__ = "quiz_sessions"

    id = Column(Integer, primary_key=True, index=True)
    usuario_nombre = Column(String, nullable=True)
    fecha_inicio = Column(DateTime(timezone=True), server_default=func.now())
    fecha_fin = Column(DateTime(timezone=True), nullable=True)
    puntuacion_total = Column(Integer, default=0)
    preguntas_respondidas = Column(Integer, default=0)
    preguntas_correctas = Column(Integer, default=0)
    estado = Column(String, default="en_progreso")
    tiempo_total_segundos = Column(Integer, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
