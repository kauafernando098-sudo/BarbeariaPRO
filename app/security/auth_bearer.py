from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.auth.jwt_handler import verificar_token


class JWTBearer(HTTPBearer):

    async def __call__(self, request: Request):

        credenciais: HTTPAuthorizationCredentials = await super().__call__(request)

        if credenciais:

            token = credenciais.credentials

            payload = verificar_token(token)

            return payload

        raise HTTPException(
            status_code=403,
            detail="Token inválido"
        )