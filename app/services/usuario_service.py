from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.usuario_model import UsuarioModel

import bcrypt


from app.auth.jwt_handler import criar_token


def login_usuario(login, db: Session):

    usuario = db.query(
        UsuarioModel
    ).filter(
        UsuarioModel.username == login.username
    ).first()

    if not usuario:

        raise HTTPException(
            status_code=401,
            detail="Usuário não encontrado"
        )

    senha_correta = bcrypt.checkpw(
        login.senha.encode("utf-8"),
        usuario.senha.encode("utf-8")
    )

    if not senha_correta:

        raise HTTPException(
            status_code=401,
            detail="Senha incorreta"
        )

    token = criar_token({

        "sub": usuario.username,

        "role": usuario.role

    })

    return {

        "access_token": token,

        "token_type": "bearer"

    }





def criar_usuario(usuario, db: Session):

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


