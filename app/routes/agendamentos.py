from fastapi import APIRouter, Depends, Query, Request
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.security.api_key import validar_api_key
from app.auth.auth_bearer import JWTBearer
from app.models.agendamento import Agendamento
from app.models.agendamento import(
    Agendamento,
   
    
)
from app.services.agendamento_service import (
    listar_agendamentos,
    criar_agendamento,
    cancelar_agendamento,
    confirmar_agendamento,
    deletar_agendamento
)

router = APIRouter()

@router.get("/")
async def listar(
    cliente: str = Query(None),
    barbeiro: str = Query(None),
    limit: int = 100,
    offset: int = 0,
    db: Session = Depends(get_db)
):

    return listar_agendamentos(
        db,
        cliente,
        barbeiro,
        limit,
        offset
    )
    


  
@router.post(
    "/",
    dependencies=[Depends(JWTBearer())]
)
async def criar(
    agendamento: Agendamento,
    request: Request,
    api_key: str = Depends(validar_api_key),
    db: Session = Depends(get_db)
):

    token_data = request.state.user

    username = token_data.get("sub")

    return criar_agendamento(
        agendamento,
        db,
        username
    )

@router.patch(
    "/{agendamento_id}/cancelar",
    dependencies=[Depends(JWTBearer())]
)
def cancelar(
    agendamento_id: int,
    db: Session = Depends(get_db)
):
    return cancelar_agendamento(
        agendamento_id,
        db
    )
@router.patch(
    "/{agendamento_id}/confirmar"
)
async def confirmar(
    agendamento_id: int,
    request: Request,
    db: Session = Depends(get_db)
):

    usuario = await JWTBearer().__call__(request)

    if usuario["role"] != "admin":

        raise HTTPException(
            status_code=403,
            detail="Sem permissão"
        )

    return confirmar_agendamento(
        agendamento_id,
        db
    )
    
    

def confirmar(
    agendamento_id: int,
    db: Session = Depends(get_db)
):
    return confirmar_agendamento(
        agendamento_id,
        db
    )

@router.delete("/{agendamento_id}")
def deletar(
    agendamento_id: int,
    db: Session = Depends(get_db)
):
    return deletar_agendamento(
        agendamento_id,
        db
    )

@router.delete("/{id}")
async def deletar(
    id: int,
    db: Session = Depends(get_db)
):

    return deletar_agendamento(
        id,
        db
    )