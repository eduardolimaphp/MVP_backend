# 🥖 Padaria API

Essa API foi desenvolvida para gerenciar os principais recursos de uma padaria: produtos, vendas e clientes. Ela utiliza Flask e SQLAlchemy para a manipulação e consulta ao banco de dados e conta com uma documentação OpenAPI integrada.

## 📜 Principais Recursos

- **Produtos**: Permite listar, criar, atualizar e deletar produtos com detalhes como nome, preço, quantidade e data de inserção.
- **Vendas**: Administra as vendas, incluindo detalhes sobre o produto vendido, cliente, quantidade vendida, data e comentários.
- **Clientes**: Gestão dos dados dos clientes, como nome, data de cadastro, e-mail e telefone.

## 📋 Índice

- [Descrição](#descrição)
- [Instalação e Configuração](#instalação-e-configuração)
  - [Ambiente Virtual](#ambiente-virtual)
  - [Dependências](#dependências)
- [Estrutura do Projeto](#estrutura-do-projeto)
  - [App.py](#apppy)
  - [Model](#model)
  - [Schemas](#schemas)
- [Uso](#uso)
- [Endpoints](#endpoints)

## 📜 Descrição

Esta API foi concebida para simplificar o gerenciamento de uma padaria, proporcionando facilidade na gestão de produtos, vendas e clientes.

## 🚀 Instalação e Configuração

### Ambiente Virtual

1️⃣ Para evitar conflitos entre bibliotecas, utilize um ambiente virtual:

```bash
# Instale o virtualenv
pip install virtualenv

# Crie um ambiente virtual chamado 'env'
virtualenv env

# Ative o ambiente virtual
# No Windows:
env\Scripts\activate

# No Linux ou MacOS:
source env/bin/activate

```

Dependências
2️⃣ Com o ambiente virtual ativado, instale as dependências:

pip install -r requirements.txt


📂 Estrutura do Projeto
App.py
O arquivo app.py é o ponto de entrada da nossa API, configurando o servidor e definindo rotas para os diversos endpoints.

Model
A pasta model contém modelos de dados que representam as tabelas no banco de dados.

Schemas
Dentro da pasta schemas, encontram-se esquemas para serialização e deserialização dos objetos, garantindo sua conversão correta para JSON.

🖥 Uso
Depois de concluir a instalação e configuração, inicie a API e explore seus endpoints!

🌐 Endpoints
A seguir, estão listados os principais endpoints da API:

/produtos: GET, POST, PUT, DELETE para gerenciamento de produtos.
/vendas: GET, POST, PUT, DELETE para administração de vendas.
/clientes: GET, POST, PUT, DELETE para gestão de clientes.
