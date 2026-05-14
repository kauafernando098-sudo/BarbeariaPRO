from fastapi import HTTPException
import bcrypt
from app.models.usuario_model import UsuarioModel
from fastapi import APIRouter
from sqlalchemy.orm import Session



from sqlalchemy.orm import Session

from app.models.usuario import Usuario

from app.models.login import Login

from app.auth.jwt_handler import criar_token


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
  

    db.add(novo_usuario)

    db.commit()

    db.refresh(novo_usuario)

    return {
        "mensagem": "Usuário criado com sucesso"
    }


def login_usuario(
    login: Login,
    db: Session
):

    usuario = db.query(
        UsuarioModel
    ).filter(
        UsuarioModel.username == login.username
    ).first()

    if not usuario:

        raise HTTPException(
            status_code=401,
            detail="Usuário ou senha inválidos"
        )

    if not bcrypt.checkpw(
        login.senha.encode("utf-8"),
        usuario.senha.encode("utf-8")
    ):

        raise HTTPException(
            status_code=401,
            detail="Usuário ou senha inválidos"
        )

    token = criar_token({
        "sub": usuario.username,
        "role": usuario.role
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }