from fastapi import APIRouter, Depends, HTTPException

from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.models.usuario_model import UsuarioModel
from app.database.connection import get_db

from app.models.usuario import Usuario

from app.services.usuario_service import criar_usuario
from app.models.login import Login

from app.services.usuario_service import (
    criar_usuario,
    login_usuario
)


router = APIRouter()


@router.post("/")
def criar_usuario(usuario, db):

    usuario_existente = db.query(
        UsuarioModel
    ).filter(
        UsuarioModel.username == usuario.username
    ).first()

    if usuario_existente:

        raise HTTPException(
            status_code=400,
            detail="Essa conta já existe"
        )

    senha_hash = bcrypt.hashpw(
        usuario.senha.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

    novo_usuario = UsuarioModel(
        username=usuario.username,
        senha=senha_hash,
        role=usuario.role
    )

    db.add(novo_usuario)

    db.commit()

    db.refresh(novo_usuario)

    return {
        "mensagem": "Usuário criado com sucesso"
    }
@router.post("/login")
def login(
    login: Login,
    db: Session = Depends(get_db)
):

    return login_usuario(
        login,
        db
    )


def criar_usuario(usuario, db):

    usuario_existente = db.query(
        UsuarioModel
    ).filter(
        UsuarioModel.username == usuario.username
    ).first()

    if usuario_existente:

        raise HTTPException(
            status_code=400,
            detail="Essa conta já existe"
        )
    if not usuario:
        raise HTTPException(
            status_code=401,
            detail="Usuário não encontrado"
        )
    
    if len(usuario.senha) < 6:
        raise HTTPException(
            status_code=400,
            detail="A senha deve conter pelo menos 6 caracteres"
        )

  