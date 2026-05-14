from datetime import datetime, timedelta
from fastapi import HTTPException
from jose import JWTError
from jose import jwt

SECRET_KEY = "segredo-super-forte"
ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 60


def criar_token(dados: dict):

    dados_copia = dados.copy()

    expiracao = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    dados_copia.update({
        "exp": expiracao
    })

    token = jwt.encode(
        dados_copia,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token



def verificar_token(token: str):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload
    except JWTError:

        raise HTTPException(
            status_code=403,
            detail="Token inválido"
        )

        


    