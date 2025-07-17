from app.db.session import engine
from app.db.base import Base
from app import models  # importa todos los modelos

def init_db():
    Base.metadata.create_all(bind=engine)
    print("✔ Base de datos creada correctamente.")

if __name__ == "__main__":
    init_db()
