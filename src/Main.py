import os

from flask import Flask, render_template, session
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv, find_dotenv
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_cors import CORS, cross_origin
from src.Controller.receitasController import receitabp, get_recipes

from src.Controller.ingredientesController import ingredientebp, get_ingredients


from src.Model.receitaModel import db as receita_db




load_dotenv(find_dotenv()) 

try:
    template_dir = os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    template_dir = os.path.join(template_dir, 'src')
    template_dir = os.path.join(template_dir, 'Viewer')
   
    app = Flask(__name__, template_folder=template_dir, static_folder=template_dir)
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    _USERNAME = os.getenv('MARIA_USERNAME')
    _PASSWORD = os.getenv('MARIA_PASSWORD')
    _DATABASE = os.getenv('MARIA_DATABASE')
    _HOST = os.getenv('MARIA_HOST')
    _PORT = os.getenv('MARIA_PORT')

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{_USERNAME}:{_PASSWORD}@{_HOST}:{_PORT}/{_DATABASE}'
    

   
    receita_db.init_app(app)
    


    app.wsgi_app = ProxyFix(app.wsgi_app)

    
    app.register_blueprint(receitabp)
    app.register_blueprint(ingredientebp)


except Exception as error:
    print(f'Erro: {error}')


def init_database():
    db = SQLAlchemy(app)
    engine = db.create_engine(f'mysql+pymysql://{_USERNAME}:{_PASSWORD}@{_HOST}:{_PORT}', {})
    try:
        engine.execute(f"CREATE DATABASE {_DATABASE}")
    except Exception as error:
        print(error)
        pass

    with app.app_context():
        
        receita_db.create_all()
        
       


@app.route('/')
@cross_origin()
def index():
    try:
        ingredients = get_ingredients()
       
    except Exception as error:
        print('error', error)
        ingredients = []
        
    try:
        recipes = get_recipes()
    except Exception as error:
        print('error', error)
        recipes = []

        
    data = {'ingredients': ingredients, 'recipes': recipes}
    print(data)
    return render_template('dashboard/dashboard.html', title='Dashboard', data=data)

