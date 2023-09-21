from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from typing import Optional

from model.base import Base

class Cliente(Base):
    __tablename__ = "cliente"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome_cliente: Mapped[str] = mapped_column(String(100), nullable=False)
    data_de_cadastro: Mapped[datetime] = mapped_column(nullable=False)
    email_cliente: Mapped[str] = mapped_column(String(100), nullable=False)
    telefone_cliente: Mapped[str] = mapped_column(String(100), nullable=False)