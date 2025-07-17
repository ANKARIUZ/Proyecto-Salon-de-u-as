from fastapi import FastAPI
from app.api.v1 import auth, users, citas

app = FastAPI()

# Incluir rutas
app.include_router(auth.router, prefix="/api/v1/auth")
app.include_router(users.router, prefix="/api/v1/users")
app.include_router(citas.router, prefix="/api/v1/citas")