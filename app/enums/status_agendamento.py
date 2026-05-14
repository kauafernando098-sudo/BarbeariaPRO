from  enum import Enum
class StatusAgendamento(str, Enum):
    PENDENTE = "PENDENTE"
    COMFIRMADO = "CONFIRMADO"
    CANCELADO = "CANCELADO"
    FINALIZADO = "FINALIZADO"