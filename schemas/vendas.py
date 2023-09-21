from pydantic import BaseModel
from datetime import datetime
from typing import List
from model.vendas import Vendas

class VendasViewSchema(BaseModel):
    """VendasViewSchema - Schema para visualização de vendas"""
    id: int = 1
    produto_id: int = 1
    cliente_id: int = 1
    quantidade_venda: int = 1
    data_da_venda: datetime = datetime.now()
    comentario: str = "Venda realizada com sucesso, cliente satisfeito."

class ListarVendasViewSchema(BaseModel):
    """VendasViewSchema - Schema para visualização de Vendas"""
    vendas: List[VendasViewSchema]

class VendasCreateSchema(BaseModel):
    """VendasCreateSchema - Schema para criação de registros de Venda"""
    produto_id: int = 1
    cliente_id: int = 1
    quantidade_venda: int = 1
    data_da_venda: datetime = datetime.now()
    comentario: str = "Venda realizada com sucesso, cliente satisfeito."

class VendasUpdateSchema(BaseModel):
    """VendasUpdateSchema - Schema para atualização de registros de Venda"""
    produto_id: int = 1
    cliente_id: int = 1
    quantidade_venda: int = 1
    data_da_venda: datetime = datetime.now()
    comentario: str = "Venda realizada com sucesso, cliente satisfeito."

class VendasDeleteSchema(BaseModel):
    """VendasDeleteSchema - Schema para remoção de registros de Venda"""
    id: int = 1

class VendasPathSchema(BaseModel):
    """VendasPathSchema - Schema para busca de registros de Venda"""
    id: int = 1

def get_vendas(vendas: List[Vendas]):
    """get_produtos_view_schema - Retorna lista de registros de Vendas"""
    
    lista_vendas = []
    for venda in vendas:
        vendaDict = {
            "id": venda.id,
            "produto_id": venda.produto_id,
            "cliente_id": venda.cliente_id,
            "quantidade_venda": venda.quantidade_venda,
            "data_da_venda": venda.data_da_venda,
            "comentario": venda.comentario
        }

        lista_vendas.append(vendaDict)

    return {
        "vendas": lista_vendas
    }

def get_vendas_por_id(venda: Vendas):
    """get_venda_view_schema - Retorna venda por ID"""
    return {
        "id": venda.id,
        "produto_id": venda.produto_id,
        "cliente_id": venda.cliente_id,
        "quantidade_venda": venda.quantidade_venda,
        "data_da_venda": venda.data_da_venda,
        "comentario": venda.comentario
    }