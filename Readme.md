# Sistema de Receitas

## Aluno
- Vitor Leandro Amorim

## Objetivo
- Desenvolver um sistema Web para criação de receitas em Python
## Videos apresentado o projeto
Video 1 - https://youtu.be/lzddPrCsVRQ
Video 2 - https://youtu.be/CjNLXmYCQxk
## Tecnologias
- Mariadb
- Flask
- SQLAlchemy
- Jinja2
- Gunicorn
- HTML5, CSS e Javascript

# Configuração

## Requerimentos mínimos
- Python V3.6 ou >
- Maria Database

## Iniciar projeto

- Clonar e atualizar repositório
- git clone https://github.com/MaguinhoD/Sistema_de_Receitas

- cd Sistema_de_Receitas
- git checkout master
- git pull

## Inicializando ambiente virtual
- (caso esteja em um linux, apt-get install python-pip para instalar a biblioteca pip)
- pip install venv ( caso não tenha a biblioteca venv instalada)
- python -m venv lib
- lib\Scripts\activate
- lib\bin\activate (caso esteja em um linux)
 
## Instalação das dependências

- pip install -r requisitos.txt

## Configurando ambiente

- Abre o HeideSQL e configure o Mariadb de acordo com as informações no arquivo .env

MARIA_DATABASE=Receitas                                                                                                                                                          
 MARIA_HOST=127.0.0.1                                                                                                                                                             
 MARIA_PORT=3306                                                                                                                                                                   
 MARIA_USERNAME=root                                                                                                                                                               
 MARIA_PASSWORD=123456                                                                                                                                                             
- A primeira vez em que rodar o código digite:

python app.py init_db

- Nas próximas vezes não é necessario iniciar o banco de dados:

python app.py

- Assim que aparecer a mensagem, é só acessar o link da aplicação:

Serving Flask app "main" (lazy loading)                                                                                                                                                          
 Environment: production                                                                                                                                                          
 WARNING: This is a development server. Do not use it in a production deployment.                                                                                                                                                          
 Use a production WSGI server instead.                                                                                                                                                          
 Debug mode: off                                                                                                                                                                   
 Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
