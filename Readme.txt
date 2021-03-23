<h1> Receitas <\h1>

<h2> Aluno <\h2>
Vitor Leandro Amorim

Objetivo
Desenvolver um sistema Web para criação de receitas em Python
Tecnologias
MySQL
Flask
SQLAlchemy
Jinja2
Gunicorn
HTML5, CSS e Javascript
Configuração
Requerimentos mínimos
Python V3.6 ou >
MySQL Database
Iniciar projeto
Clonar e atualizar repositório
git clone https://github.com/fabsvas/recipp-app.git
cd recipp-app
git checkout master
git pull
Inicializando ambiente virtual
 python -m venv env
Instalação das dependências
pip install -r requirements.txt
Configurando ambiente
Configure a conexão com o MySQL no arquivo .env localizado na raiz do projeto de acordo com o exemplo a seguir

MYSQL_DATABASE=receitas
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USERNAME=root
MYSQL_PASSWORD=1234554321