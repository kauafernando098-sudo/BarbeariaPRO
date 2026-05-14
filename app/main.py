from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.base import Base
from app.database.connection import engine

from app.routes.usuarios import router as usuarios_router
from app.routes.agendamentos import router as agendamentos_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://barbearia-pro-pi.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(usuarios_router)
app.include_router(agendamentos_router)

@app.get("/")
def home():

    return {
        "mensagem": "Servidor funcionando"
    }