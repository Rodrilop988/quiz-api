from sqlalchemy import Column, Integer, String, Boolean, DateTime, JSON, Text
from sqlalchemy.sql import func
from app.database import Base

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    pregunta = Column(String, nullable=False)
    opciones = Column(JSON, nullable=False)
    respuesta_correcta = Column(Integer, nullable=False)
    explicacion = Column(Text, nullable=True)
    categoria = Column(String, index=True)
    dificultad = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    is_active = Column(Boolean, default=True)
