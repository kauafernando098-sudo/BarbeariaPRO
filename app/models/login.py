from pydantic import BaseModel


class Login(BaseModel):

    username: str

    senha: str

    role:str = "cliente"