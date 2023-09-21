from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from typing import Optional

from model.base import Base

class Produto(Base):
    __tablename__ = "produto"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    quantidade: Mapped[int] = mapped_column(nullable=False)
    preco: Mapped[float] = mapped_column(nullable=False)
    data_insercao: Mapped[str] = mapped_column(nullable=False)
