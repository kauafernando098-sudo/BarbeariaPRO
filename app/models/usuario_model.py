from sqlalchemy import Column, Integer, String

from app.database.base import Base


class UsuarioModel(Base):

    __tablename__ = "usuarios"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    username = Column(
        String,
        unique=True
    )

    senha = Column(String)
    role = Column(String, default="cliente")