from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Cita(Base):
    __tablename__ = "citas"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("users.id"))
    fecha = Column(DateTime, nullable=False)
    servicio = Column(String, nullable=False)
    estado = Column(String, default="pendiente")

    cliente = relationship("User", back_populates="citas")
