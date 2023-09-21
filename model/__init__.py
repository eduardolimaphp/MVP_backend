from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine
import os

#importando elementos definidos no modelo
from model.base import Base

#importando model de produtos
from model.produto import Produto

#importando model de vendas
from model.vendas import Vendas

#importando model de clientes
from model.clientes import Cliente

#Nome da pasta do banco
db_path = "database/"

#Verifica se a pasta do banco não existe
if not os.path.exists(db_path):
    os.makedirs(db_path)

#url do banco
db_url = 'sqlite:///%s/db.sqlite3' % db_path

#cria a engine de conexão com o banco
engine = create_engine(db_url, echo=False)

#cria o banco se ele não esxitir
if not database_exists(engine.url):
    create_database(engine.url)

#cria as tabelas do banco, caso não existam
Base.metadata.create_all(engine)