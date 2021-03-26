import os

from flask import Flask, render_template, session
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv, find_dotenv
from werkzeug.middleware.proxy_fix import ProxyFix


from src.Controller.receitasController import receitabp, get_recipes

from src.Controller.ingredientesController import ingredientebp, get_ingredients


from src.Model.receitaModel import db as receita_db
from src.Model.IngredienteModel import db as ingrediente_db
from src.Model.IngredientedaReceitaModel import db as ingredientereceita_db



load_dotenv(find_dotenv()) 

try:
    template_dir = os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    template_dir = os.path.join(template_dir, 'src')
    template_dir = os.path.join(template_dir, 'Viewer')
   
    app = Flask(__name__, template_folder=template_dir, static_folder=template_dir)

    _USERNAME = os.getenv('MARIA_USERNAME')
    _PASSWORD = os.getenv('MARIA_PASSWORD')
    _DATABASE = os.getenv('MARIA_DATABASE')
    _HOST = os.getenv('MARIA_HOST')
    _PORT = os.getenv('MARIA_PORT')

    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{_USERNAME}:{_PASSWORD}@{_HOST}:{_PORT}/{_DATABASE}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    
    receita_db.init_app(app)
    ingrediente_db.init_app(app)
    ingredientereceita_db.init_app(app)

    app.wsgi_app = ProxyFix(app.wsgi_app)

    
    app.register_blueprint(receitabp)
    app.register_blueprint(ingredientebp)


except Exception as error:
    print(f'Erro: {error}')


def init_database(appFlask):
    db = SQLAlchemy(appFlask)
    engine = db.create_engine(f'mysql+pymysql://{_USERNAME}:{_PASSWORD}@{_HOST}:{_PORT}', {})
    try:
        engine.execute(f"CREATE DATABASE {_DATABASE}")
    except Exception as error:
        print(error)
        pass

    with appFlask.app_context():
        
        receita_db.create_all()
        ingrediente_db.create_all()
        ingredientereceita_db.create_all()


@app.route('/')
def index():
    try:
        ingredients = get_ingredients()
        recipes = get_recipes()
    except Exception as error:
        print('error', error)
        ingredients = []
        recipes = []
    data = {'ingredients': ingredients, 'recipes': recipes}
    print(data)
    return render_template('dashboard/dashboard.html', title='Dashboard', data=data)

