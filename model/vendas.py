from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from typing import Optional

#importando modelo base
from model.base import Base

#importando tabela produto
from model.produto import Produto

#importando tabela cliente
from model.produto import Produto

class Vendas(Base):
    __tablename__ = "vendas"

    id: Mapped[int] = mapped_column(primary_key=True)

    produto_id: Mapped[int] = mapped_column(ForeignKey("produto.id"), nullable=False)
    produto: Mapped["Produto"] = relationship()

    cliente_id: Mapped[int] = mapped_column(ForeignKey("cliente.id"), nullable=False)
    cliente: Mapped["Cliente"] = relationship()


    quantidade_venda: Mapped[int] = mapped_column(nullable=False)
    data_da_venda: Mapped[datetime] = mapped_column(nullable=False)
    comentario: Mapped[Optional[str]] = mapped_column(String(200))