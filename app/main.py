from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from app.database.base import Base
from app.database.connection import engine
from app.routes import usuarios
from app.routes import agendamentos

from app.routes.agendamentos import router as agendamentos_router
from app.routes.usuarios import router as usuarios_router

from app.models.agendamento_model import AgendamentoModel
from app.models.usuario_model import UsuarioModel


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
app.include_router(
    usuarios.router
)

app.include_router(
    agendamentos.router
)
app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)


app.include_router(
    agendamentos_router,
    prefix="/agendamentos",
    tags=["Agendamentos"]
)

app.include_router(
    usuarios_router,
    prefix="/usuarios",
    tags=["Usuários"]
)


@app.get("/")
def home():

    return {
        "mensagem": "Servidor funcionando"
    }
