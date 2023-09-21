from pydantic import BaseModel
from datetime import datetime
from typing import List
from model.clientes import Cliente

class ClientesViewSchema(BaseModel):
    """ClientesViewSchema - Schema para visualização de clientes"""
    id: int = 1
    nome_cliente: str = "João da Silva"
    data_de_cadastro: datetime = datetime.now()
    email_cliente: str = "joao@gmail.com"
    telefone_cliente: str = "11999999999"

class ListarClientesViewSchema(BaseModel):
    """ClientesViewSchema - Schema para visualização de Clientes"""
    clientes: List[ClientesViewSchema]

class ClientesCreateSchema(BaseModel):
    """ClientesCreateSchema - Schema para criação de cadastro de cliente"""
    nome_cliente: str = "João da Silva"
    data_de_cadastro: datetime = datetime.now()
    email_cliente: str = "joao@gmail.com"
    telefone_cliente: str = "11999999999"

class ClienteUpdateSchema(BaseModel):
    """ClienteUpdateSchema - Schema para atualização de dados do cliente"""
    nome_cliente: str = "João da Silva"
    data_de_cadastro: datetime = datetime.now()
    email_cliente: str = "joao@gmail.com"
    telefone_cliente: str = "11999999999"

class ClientesDeleteSchema(BaseModel):
    """ClientesDeleteSchema - Schema para remoção de cadastro de cliente"""
    id: int = 1

class ClientesPathSchema(BaseModel):
    """ClientesPathSchema - Schema para busca de cadastro de clientes"""
    id: int = 1

def get_clientes(clientes: List[Cliente]):
    """get_clientes_view_schema - Retorna lista de clientes"""
        
    lista_clientes = []
    for cliente in clientes:
            clienteDict = {
                "id": cliente.id,
                "nome_cliente": cliente.nome,
                "data_de_cadastro": cliente.data_de_cadastro,
                "email_cliente": cliente.email,
                "telefone_cliente": cliente.telefone
            }
    
            lista_clientes.append(clienteDict)
    
    return {
        "clientes": lista_clientes
    }

def get_clientes_por_id(cliente: Cliente):
    """get_cliente_view_schema - Retorna cadastro de cliente por ID"""
    return {
        "id": cliente.id,
        "nome_cliente": cliente.nome,
        "data_de_cadastro": cliente.data_de_cadastro,
        "email_cliente": cliente.email,
        "telefone_cliente": cliente.telefone
    }