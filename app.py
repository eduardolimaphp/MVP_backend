from flask import request, redirect
from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS

from sqlalchemy.orm import Session
from model import engine

#importando models
from model.produto import Produto
from model.vendas import Vendas
from model.clientes import Cliente

#importando schemas
from schemas.produto import *
from schemas.vendas import *
from schemas.clientes import *

#importando schema de erro
from schemas.error import ErrorSchema

#importando funções de retorno e documentação
info = Info(title="Padaria", version="1.0.0")
app = OpenAPI(__name__, info=info)

CORS(app)

#criando tags de documentação
home_tag = Tag(name="Home", description="Homepage")
produto_tag = Tag(name="Produto", description="Produtos")
vendas_tag = Tag(name="Vendas", description="Vendas")
clientes_tag = Tag(name="Clientes", description="Clientes")

#criando endpoints
@app.get("/", tags=[home_tag])
def home():
    """Este endpoint é a página inicial da API"""
    return redirect("/openapi")

#criando endpoints de produtos
@app.get("/produtos", tags=[produto_tag],
         responses={200:ListarProdutosViewSchema, 404: ErrorSchema})
def listar_produtos():
    """Este endpoint retorna uma lista de produtos"""
    with Session(engine) as session:
        produtos = session.query(Produto).all()
        if not produtos:
            return {"message": "Nenhum produto encontrado"}, 404
        return get_produtos(produtos)
    
@app.get("/produtos/<int:id>", tags=[produto_tag],
            responses={200:ProdutoViewSchema, 404: ErrorSchema})
def listar_produto_por_id(path: ProdutosPathSchema):
    """Este endpoint retorna um produto por ID"""
    with Session(engine) as session:
        produto = session.query(Produto).filter(Produto.id == path.id).first()
        if not produto:
            return {"message": "Produto não encontrado"}, 404
        return get_produto_por_id(produto)
    

@app.post("/produtos", tags=[produto_tag],
            responses={201:ProdutoViewSchema, 400: ErrorSchema})
def criar_produto(form: ProdutosCreateSchema):
    """Este endpoint cria um produto"""

    try:
        with Session(engine) as session:
            novo_produto = Produto(nome=form.nome_produto, preco=form.preco_produto, quantidade=form.quantidade_produto, data_insercao=form.data_de_cadastro)
            session.add(novo_produto)
            session.commit()
            return get_produto_por_id(novo_produto), 201
    except Exception as e:
        error_criar_produto = "Erro ao criar produto, verifique os dados inseridos."
        return {"message": error_criar_produto}, 400
    

@app.put("/produtos/<int:id>")
def atualizar_produto(id: int):
    """Este endpoint atualiza a quantidade de um produto"""

    form = request.json  # Obter o corpo JSON do pedido

    if not form or 'quantidade_produto' not in form:
        return {"message": "Dados de entrada inválidos."}, 400

    try:
        with Session(engine) as session:
            produto_atualizado = session.query(Produto).filter(Produto.id == id).first()

            if not produto_atualizado:
                return {"message": "Produto não encontrado"}, 404

            produto_atualizado.quantidade = form['quantidade_produto']
            session.commit()

            return get_produto_por_id(produto_atualizado.id)
    except Exception as e:
        return {"message": "Erro ao atualizar produto, verifique os dados inseridos."}, 400



@app.put("/produtos/<int:id>/completo", tags=[produto_tag],
            responses={200:ProdutoViewSchema, 400: ErrorSchema, 404: ErrorSchema})
def atualizar_produto_id_completo(form: ProdutosUpdateSchema):
    """Este endpoint atualiza um produto"""
    try:
        with Session(engine) as session:
            produto_atualizado = session.query(Produto).filter(Produto.id == form.id).first()
            if not produto_atualizado:
                return {"message": "Produto não encontrado"}, 404
            produto_atualizado.nome = form.nome_produto
            produto_atualizado.preco = form.preco_produto
            produto_atualizado.quantidade = form.quantidade_produto
            produto_atualizado.data_insercao = form.data_de_cadastro
            session.commit()
            return get_produto_por_id(produto_atualizado)
    except Exception as e:
        error_atualizar_produto = "Erro ao atualizar produto, verifique os dados inseridos."
        return {"message": error_atualizar_produto}, 400
   
@app.delete("/produtos/removeregistro/<int:id>", tags=[produto_tag],
            responses={200:ProdutoViewSchema, 404: ErrorSchema})
def deletar_produto_completo(path: ProdutosDeleteSchema):
    """Este endpoint deleta um produto por completo"""
    with Session(engine) as session:
        produto = session.query(Produto).filter(Produto.id == path.id).first()
        if not produto:
            return {"message": "Produto não encontrado"}, 404
        session.delete(produto)
        session.commit()
        return get_produto_por_id(produto)

@app.delete("/produtos/<int:id>", tags=[produto_tag],
            responses={200:ProdutoViewSchema, 404: ErrorSchema})
def deletar_produto(path: ProdutosDeleteSchema):
    """Este endpoint decrementa a quantidade do produto e deleta se a quantidade for zero."""
    with Session(engine) as session:
        produto = session.query(Produto).filter(Produto.id == path.id).first()
        if not produto:
            return {"message": "Produto não encontrado"}, 404

        if produto.quantidade > 1:
            produto.quantidade -= 1
            session.commit()
        else:
            session.delete(produto)
            session.commit()

        return get_produto_por_id(produto)


#criando endpoints de vendas
@app.get("/vendas", tags=[vendas_tag],
            responses={200:ListarVendasViewSchema, 404: ErrorSchema})
def listar_vendas():
    """Este endpoint retorna uma lista de vendas"""
    with Session(engine) as session:
        vendas = session.query(Vendas).all()
        if not vendas:
            return {"message": "Nenhuma venda encontrada"}, 404
        return get_vendas(vendas)
    
@app.get("/vendas/<int:id>", tags=[vendas_tag],
            responses={200:VendasViewSchema, 404: ErrorSchema})
def listar_venda_por_id(path: VendasPathSchema):
    """Este endpoint retorna uma venda por ID"""
    with Session(engine) as session:
        venda = session.query(Vendas).filter(Vendas.id == path.id).first()
        if not venda:
            return {"message": "Venda não encontrada"}, 404
        return get_vendas_por_id(venda)

@app.post("/vendas", tags=[vendas_tag],
            responses={201:VendasViewSchema, 400: ErrorSchema})
def criar_venda(form: VendasCreateSchema):
    """Este endpoint cria uma venda"""
    try:
        with Session(engine) as session:
            nova_venda = Vendas(produto_id=form.produto_id, cliente_id=form.cliente_id, quantidade_venda=form.quantidade_venda, data_da_venda=form.data_da_venda, comentario=form.comentario)
            session.add(nova_venda)
            session.commit()
            return get_vendas_por_id(nova_venda), 201
    except Exception as e:
        error_criar_venda = "Erro ao criar venda, verifique os dados inseridos."
        return {"message": error_criar_venda}, 400

@app.put("/vendas/<int:id>", tags=[vendas_tag],
            responses={200:VendasViewSchema, 400: ErrorSchema, 404: ErrorSchema})
def atualizar_venda(form: VendasUpdateSchema):
    """Este endpoint atualiza uma venda"""
    try:
        with Session(engine) as session:
            venda_atualizada = session.query(Vendas).filter(Vendas.id == form.id).first()
            if not venda_atualizada:
                return {"message": "Venda não encontrada"}, 404
            venda_atualizada.produto_id = form.produto_id
            venda_atualizada.cliente_id = form.cliente_id
            venda_atualizada.quantidade_venda = form.quantidade_venda
            venda_atualizada.data_da_venda = form.data_da_venda
            venda_atualizada.comentario = form.comentario
            session.commit()
            return get_vendas_por_id(venda_atualizada)
    except Exception as e:
        error_atualizar_venda = "Erro ao atualizar venda, verifique os dados inseridos."
        return {"message": error_atualizar_venda}, 400

@app.delete("/vendas/<int:id>", tags=[vendas_tag],
            responses={200:VendasViewSchema, 404: ErrorSchema})
def deletar_venda(path: VendasDeleteSchema):
    """Este endpoint deleta uma venda"""
    with Session(engine) as session:
        venda = session.query(Vendas).filter(Vendas.id == path.id).first()
        if not venda:
            return {"message": "Venda não encontrada"}, 404
        session.delete(venda)
        session.commit()
        return get_vendas_por_id(venda)

#criando endpoints de clientes
@app.get("/clientes", tags=[clientes_tag],
            responses={200:ListarClientesViewSchema, 404: ErrorSchema})
def listar_clientes():
    """Este endpoint retorna uma lista de clientes"""
    with Session(engine) as session:
        clientes = session.query(Cliente).all()
        if not clientes:
            return {"message": "Nenhum cliente encontrado"}, 404
        return get_clientes(clientes)

@app.get("/clientes/<int:id>", tags=[clientes_tag],
            responses={200:ClientesViewSchema, 404: ErrorSchema})
def listar_cliente_por_id(path: ClientesPathSchema):
    """Este endpoint retorna um cliente por ID"""
    with Session(engine) as session:
        cliente = session.query(Cliente).filter(Cliente.id == path.id).first()
        if not cliente:
            return {"message": "Cliente não encontrado"}, 404
        return get_clientes_por_id(cliente)

@app.post("/clientes", tags=[clientes_tag],
            responses={201:ClientesViewSchema, 400: ErrorSchema})
def criar_cliente(form: ClientesCreateSchema):
    """Este endpoint cria um cliente"""
    try:
        with Session(engine) as session:
            novo_cliente = Cliente(nome=form.nome_cliente, data_de_cadastro=form.data_de_cadastro, email=form.email_cliente, telefone=form.telefone_cliente)
            session.add(novo_cliente)
            session.commit()
            return get_clientes_por_id(novo_cliente), 201
    except Exception as e:
        error_criar_cliente = "Erro ao criar cliente, verifique os dados inseridos."
        return {"message": error_criar_cliente}, 400

@app.put("/clientes/<int:id>", tags=[clientes_tag],
            responses={200:ClientesViewSchema, 400: ErrorSchema, 404: ErrorSchema})
def atualizar_cliente(form: ClienteUpdateSchema):
    """Este endpoint atualiza um cliente"""
    try:
        with Session(engine) as session:
            cliente_atualizado = session.query(Cliente).filter(Cliente.id == form.id).first()
            if not cliente_atualizado:
                return {"message": "Cliente não encontrado"}, 404
            cliente_atualizado.nome = form.nome_cliente
            cliente_atualizado.data_de_cadastro = form.data_de_cadastro
            cliente_atualizado.email = form.email_cliente
            cliente_atualizado.telefone = form.telefone_cliente
            session.commit()
            return get_clientes_por_id(cliente_atualizado)
    except Exception as e:
        error_atualizar_cliente = "Erro ao atualizar cliente, verifique os dados inseridos."
        return {"message": error_atualizar_cliente}, 400

@app.delete("/clientes/<int:id>", tags=[clientes_tag],
            responses={200:ClientesViewSchema, 404: ErrorSchema})
def deletar_cliente(path: ClientesDeleteSchema):
    """Este endpoint deleta um cliente"""
    with Session(engine) as session:
        cliente = session.query(Cliente).filter(Cliente.id == path.id).first()
        if not cliente:
            return {"message": "Cliente não encontrado"}, 404
        session.delete(cliente)
        session.commit()
        return get_clientes_por_id(cliente)


