from fastapi import APIRouter, Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.user import UserOut
from app.api.deps import get_db, get_current_user
from app.crud.user import get_users
from app.models.user import User

router = APIRouter()

@router.get("/", response_model=List[UserOut])
def get_users_route(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_users(db)

@router.get("/{user_id}", response_model=UserOut)
def get_user_by_id(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user