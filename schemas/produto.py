from pydantic import BaseModel
from datetime import datetime
from typing import List
from model.produto import Produto

class ProdutoViewSchema(BaseModel):
    """ProdutoViewSchema - Schema para visualização de produto"""
    id: int = 1
    nome_produto: str = "Pão de Doce de Leite"
    preco_produto: float = 1.0
    quantidade_produto: int = 1
    data_de_cadastro: str = "2021-10-10 10:10:10"

class ListarProdutosViewSchema(BaseModel):
    """ProdutosViewSchema - Schema para visualização de produtos"""
    produtos: List[ProdutoViewSchema]

class ProdutosCreateSchema(BaseModel):
    """ProdutosCreateSchema - Schema para criação de produtos"""
    nome_produto: str = "Pão de Doce de Coco"
    preco_produto: float = 1.0
    quantidade_produto: int = 2
    data_de_cadastro: str = "2021-10-10 10:10:10"

class ProdutosUpdateSchema(BaseModel):
    """ProdutosUpdateSchema - Schema para atualização de produtos"""
    nome_produto: str = "Pão de Doce de Leite"
    preco_produto: float = 1.0
    quantidade_produto: int = 2
    data_de_cadastro: str = "2021-10-10 10:10:10"

class ProdutoQUpdateSchema(BaseModel):
    """ProdutoQUpdateSchema - Schema para atualização de quantidade de produtos"""
    quantidade_produto: int = 2

class ProdutosDeleteSchema(BaseModel):
    """ProdutosDeleteSchema - Schema para remoção de produtos"""
    id: int = 1

class ProdutosPathSchema(BaseModel):
    """ProdutosPathSchema - Schema para busca de produtos"""
    busca: str

def get_produtos(produtos: List[Produto]):
    """get_produtos_view_schema - Retorna lista de produtos"""
    
    lista_produtos = []
    for produto in produtos:
        produtoDict = {
            "id": produto.id,
            "nome_produto": produto.nome,
            "preco_produto": produto.preco,
            "quantidade_produto": produto.quantidade,
            "data_de_cadastro": produto.data_insercao
        }

        lista_produtos.append(produtoDict)

    return {
        "produtos": lista_produtos
    }

def get_produto_por_id(produto: Produto):
    """get_produto_view_schema - Retorna produto por ID"""
    return {
        "id": produto.id,
        "nome_produto": produto.nome,
        "preco_produto": produto.preco,
        "quantidade_produto": produto.quantidade,
        "data_de_cadastro": produto.data_insercao
    }