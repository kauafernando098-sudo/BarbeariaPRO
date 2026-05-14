from datetime import time
from pydantic import BaseModel, Field
from app.enums.status_agendamento import StatusAgendamento

class Agendamento(BaseModel):
    cliente: str = Field(min_length=3)
    horario: time
    barbeiro: str = Field(min_length=3)

class AgendamentoResponse(BaseModel):
    id: int
    cliente: str
    horario: time
    barbeiro: str
    status: StatusAgendamento   
    class config:
        from_attributes = True
   