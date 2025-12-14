from pydantic import BaseModel
from typing import Optional

class AnswerCreate(BaseModel):
    quiz_session_id: int
    question_id: int
    respuesta_seleccionada: int
    tiempo_respuesta_segundos: Optional[int] = None

class AnswerResponse(BaseModel):
    id: int
    es_correcta: bool

    class Config:
        from_attributes = True
