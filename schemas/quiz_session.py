from pydantic import BaseModel
from typing import Optional

class QuizSessionCreate(BaseModel):
    usuario_nombre: Optional[str] = None

class QuizSessionResponse(BaseModel):
    id: int
    usuario_nombre: Optional[str]
    estado: str
    puntuacion_total: int

    class Config:
        from_attributes = True
