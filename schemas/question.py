from pydantic import BaseModel, field_validator
from typing import List, Optional

class QuestionBase(BaseModel):
    pregunta: str
    opciones: List[str]
    respuesta_correcta: int
    explicacion: Optional[str] = None
    categoria: str
    dificultad: str

    @field_validator("opciones")
    def validar_opciones(cls, v):
        if not 3 <= len(v) <= 5:
            raise ValueError("Las opciones deben ser entre 3 y 5")
        return v

    @field_validator("respuesta_correcta")
    def validar_respuesta(cls, v, info):
        opciones = info.data.get("opciones", [])
        if v < 0 or v >= len(opciones):
            raise ValueError("respuesta_correcta fuera de rango")
        return v

class QuestionCreate(QuestionBase):
    pass

class QuestionResponse(QuestionBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True
