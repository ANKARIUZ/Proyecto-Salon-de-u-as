from sqlalchemy.orm import Session
from app.models.cita import Cita
from app.schemas.cita import CitaCreate

def crear_cita(db: Session, cliente_id: int, cita_in: CitaCreate):
    db_cita = Cita(**cita_in.dict(), cliente_id=cliente_id)
    db.add(db_cita)
    db.commit()
    db.refresh(db_cita)
    return db_cita

def obtener_citas_por_usuario(db: Session, cliente_id: int):
    return db.query(Cita).filter(Cita.cliente_id == cliente_id).all()

