from pydantic import BaseModel, Field


class Usuario(BaseModel):

    username: str = Field(min_length=3)

    senha: str = Field(min_length=6)
    role: str = "cliente"

    