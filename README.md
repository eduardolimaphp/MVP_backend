# 🥖 Padaria API

🍰 Uma interface simples e eficiente para gerenciar sua padaria!

---

## 📋 Índice

- [Descrição](#-descrição)
- [Instalação e Configuração](#-instalação-e-configuração)
  - [Ambiente Virtual](#ambiente-virtual)
  - [Dependências](#dependências)
- [Estrutura do Projeto](#-estrutura-do-projeto)
  - [App.py](#app)
  - [Model](#model)
  - [Schemas](#schemas)
- [Uso](#-uso)

---

## 📜 Descrição

Esta é uma API desenvolvida para facilitar o gerenciamento de uma padaria. Com ela, os usuários podem facilmente gerenciar produtos, vendas e clientes.

---

## 🚀 Instalação e Configuração

### Ambiente Virtual

1️⃣ Evite conflitos entre bibliotecas utilizando um ambiente virtual:

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

Dependências
2️⃣ Com o ambiente virtual ativado, instale as dependências do projeto:

bash
Copy code
pip install -r requirements.txt
📂 Estrutura do Projeto

App.py
📄 app.py é o ponto de entrada da nossa API. Aqui, você encontrará a configuração inicial do servidor e as rotas para os diversos endpoints disponíveis.

Model
📁 A pasta model armazena os modelos de dados que representam as tabelas do banco de dados. Aqui, você encontrará estruturas como Produto, Vendas e Cliente.

Schemas
📁 A pasta schemas contém esquemas responsáveis pela serialização e deserialização dos objetos dos modelos. Estes esquemas garantem a conversão correta dos objetos para um formato JSON.

🖥 Uso
Após concluir as etapas de instalação, você está pronto para executar a API e explorar seus diversos endpoints!