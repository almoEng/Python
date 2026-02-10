📘 CRUD em Python com MySQL (PyMySQL)

Este projeto implementa um sistema simples de CRUD (Create, Read, Update, Delete) utilizando Python e MySQL, com comunicação direta via biblioteca PyMySQL.
O objetivo é demonstrar, de forma prática, como manipular dados em um banco relacional usando operações básicas e seguras.

🚀 Funcionalidades

O sistema realiza as seguintes operações:

Inserir dados na tabela autores

Listar todos os autores

Atualizar o nome de um autor

Excluir um autor

Menu interativo e repetitivo para facilitar o uso

O banco de dados utilizado contém duas tabelas:

autores

posts
(este projeto manipula apenas a tabela autores, mas pode ser expandido facilmente).

🛠 Tecnologias Utilizadas

Python 3

MySQL

PyMySQL (cliente para MySQL)

Banco relacional CRUD simples

📦 Instalação
1️⃣ Instale o PyMySQL
pip install pymysql

2️⃣ Configure o MySQL

Crie o banco e a tabela:

CREATE DATABASE crud_mysql;

USE crud_mysql;

CREATE TABLE autores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

3️⃣ Ajuste suas credenciais no código:
config = {
    'host': 'localhost',
    'user': 'vagner_user',
    'password': 'sua_senha',
    'database': 'crud_mysql',
    'cursorclass': pymysql.cursors.DictCursor
}

▶️ Como Executar

No terminal:

python3 seu_arquivo.py


O menu aparecerá:

Opção 1 - Inserir dados
Opção 2 - Listar dados
Opção 3 - Atualizar dados
Opção 4 - Excluir dados


Depois basta escolher o número desejado.

📂 Estrutura do Projeto
crud/
│-- crud_mysql.py  # Arquivo principal
│-- README.md

🧠 Como Funciona

Cada operação abre uma conexão com o MySQL, executa a ação desejada e fecha automaticamente.
A aplicação também valida:

Se existem autores antes de atualizar/excluir

Se o nome informado existe

Se a operação afetou registros

Tudo é feito de forma segura e organizada usando cursor() e commit().

📜 Licença

Este projeto é livre para estudos e modificações.
