from sqlalchemy import Column, Integer, String, Time
from sqlalchemy import ForeignKey

from app.database.base import Base


class AgendamentoModel(Base):

    __tablename__ = "agendamentos"

    id = Column(Integer, primary_key=True, index=True)

    cliente = Column(String)

    horario = Column(Time)

    barbeiro = Column(String)

    status = Column(String)

    usuario_id = Column(
        Integer,
        ForeignKey("usuarios.id")
    )