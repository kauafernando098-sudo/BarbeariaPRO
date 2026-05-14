from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.models.usuario import Usuario
from app.models.login import Login

from app.services.usuario_service import (
    criar_usuario,
    login_usuario
)
router = APIRouter(
    prefix="/usuarios",
    tags=["Usuários"]
)

@router.post("/")
def criar(
    usuario: Usuario,
    db: Session = Depends(get_db)
):

    return criar_usuario(
        usuario,
        db
    )


@router.post("/login")
def login(
    login: Login,
    db: Session = Depends(get_db)
):

    return login_usuario(
        login,
        db
    )