from pydantic import BaseModel
from datetime import datetime

class CitaBase(BaseModel):
    fecha: datetime
    servicio: str
    estado: str = "pendiente"

class CitaCreate(CitaBase):
    pass

class CitaOut(CitaBase):
    id: int
    cliente_id: int

    class Config:
        from_attributes = True

