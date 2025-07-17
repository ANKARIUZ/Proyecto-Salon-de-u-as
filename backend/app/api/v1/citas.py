from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_db, get_current_user
from app.schemas.cita import CitaCreate, CitaOut
from app.models.user import User
from app.crud import cita as crud_cita

router = APIRouter()

@router.post("/", response_model=CitaOut)
def crear_cita(cita_in: CitaCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud_cita.crear_cita(db, cliente_id=current_user.id, cita_in=cita_in)

@router.get("/", response_model=List[CitaOut])
def listar_mis_citas(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud_cita.obtener_citas_por_usuario(db, cliente_id=current_user.id)
