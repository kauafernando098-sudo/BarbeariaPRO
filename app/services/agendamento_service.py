from fastapi import HTTPException
from app.models.agendamento import Agendamento
from sqlalchemy.orm import Session
from datetime import time, timedelta, datetime
from app.enums.status_agendamento import StatusAgendamento
from app.models.usuario_model import UsuarioModel

from app.models.agendamento_model import AgendamentoModel


def listar_agendamentos(
    db: Session,
    username: str,
    role: str,
    status: str = None,
    ordenar: str = None,
    limit: int = 10,
    offset: int = 0
):
    usuario = db.query(
    UsuarioModel
).filter(
    UsuarioModel.username == username
).first()

    query = db.query(AgendamentoModel)

    if role != "admin":
        query = query.filter(
            AgendamentoModel.usuario_id == usuario.id
        )

        query = query.order_by(
            AgendamentoModel.horario
        )

    if ordenar == "cliente":

        query = query.order_by(
            AgendamentoModel.cliente
        )

    query = query.offset(offset).limit(limit)

    return query.all()


def criar_agendamento(
    agendamento: Agendamento,
    db: Session,
    username: str
):
    usuario = db.query(
    UsuarioModel
).filter(
    UsuarioModel.username == username
).first()
    
    novo_agendamento = AgendamentoModel(
        cliente=agendamento.cliente,
        horario=agendamento.horario,
        barbeiro=agendamento.barbeiro,
        usuario_id= usuario.id,
        status="PENDENTE"

    )

    db.add(novo_agendamento)
    db.commit()
    db.refresh(novo_agendamento)

    return {
        "mensagem": "Agendamento criado com sucesso",
    }

def listar_agendamentos(
    db,
    cliente=None,
    barbeiro=None,
    limit=100,
    offset=0
):

    query = db.query(AgendamentoModel)

    if cliente:
        query = query.filter(
            AgendamentoModel.cliente.contains(cliente)
        )

    if barbeiro:
        query = query.filter(
            AgendamentoModel.barbeiro.contains(barbeiro)
        )

    return query.offset(offset).limit(limit).all()

def cancelar_agendamento(
    agendamento_id: int,
    db: Session
):

    agendamento = db.query(
        AgendamentoModel
    ).filter(
        AgendamentoModel.id == agendamento_id
    ).first()

    if not agendamento:

        raise HTTPException(
            status_code=404,
            detail="Agendamento não encontrado"
        )

    if agendamento.status == StatusAgendamento.CANCELADO:

        raise HTTPException(
            status_code=409,
            detail="Agendamento já está cancelado"
        )

    agendamento.status = StatusAgendamento.CANCELADO

    db.commit()

    db.refresh(agendamento)

    return {
        "mensagem": "Agendamento cancelado com sucesso"
    }

def confirmar_agendamento(
    agendamento_id: int,
    db: Session
):

    agendamento = db.query(
        AgendamentoModel
    ).filter(
        AgendamentoModel.id == agendamento_id
    ).first()

    if not agendamento:

        raise HTTPException(
            status_code=404,
            detail="Agendamento não encontrado"
        )

    if agendamento.status == StatusAgendamento.CANCELADO:

        raise HTTPException(
            status_code=409,
            detail="Agendamento cancelado não pode ser confirmado"
        )

    if agendamento.status == StatusAgendamento.CONFIRMADO:

        raise HTTPException(
            status_code=409,
            detail="Agendamento já está confirmado"
        )

    agendamento.status = StatusAgendamento.CONFIRMADO

    db.commit()

    db.refresh(agendamento)

    return {
        "mensagem": "Agendamento confirmado com sucesso"
    }


def deletar_agendamento(
    agendamento_id: int,
    db: Session
):

    agendamento = db.query(
        AgendamentoModel
    ).filter(
        AgendamentoModel.id == agendamento_id
    ).first()

    if not agendamento:

        raise HTTPException(
            status_code=404,
            detail="Agendamento não encontrado"
        )

    db.delete(agendamento)

    db.commit()

    return {
        "mensagem": "Agendamento deletado com sucesso"
    }

def deletar_agendamento(id, db):

    agendamento = db.query(
        AgendamentoModel
    ).filter(
        AgendamentoModel.id == id
    ).first()

    if not agendamento:
        return {
            "erro": "Agendamento não encontrado"
        }

    db.delete(agendamento)

    db.commit()

    return {
        "mensagem": "Agendamento deletado"
    }
