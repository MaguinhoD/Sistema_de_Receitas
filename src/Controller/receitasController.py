import json
from flask import Blueprint, current_app, render_template,request,Response,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError



from src.Controller.ingredientesController import get_ingredients
from src.Model.receitaModel import Receita as ReceitaModel
from src.Model.receitaModel import ingrediente_receita as IngReceitaModel

receitabp = Blueprint('receita', __name__, url_prefix='/receitas')


@receitabp.route('/')
def index():
    recipes = get_recipes()
    return render_template('recipe/recipe.html', title='Receitas', data={'recipes': recipes})


@receitabp.route('/create', methods=['GET', 'POST'])
def create_recipe():
    if request.method == 'POST':
        name = request.form.get('name')
        ingredients = request.form.get('ingredients')
    recipes = get_recipes()
    stored_ingredients = get_ingredients()
    return render_template('recipe/create-recipe/create-recipe.html', data={'stored_ingredients': stored_ingredients, 'recipes':recipes})


@receitabp.route('/createrecipe', methods=['POST', 'GET'])
def createrecipe():
    try:

        db = SQLAlchemy(current_app)

        obj = request.json
        newReceita = ReceitaModel(name=obj['name'],category=obj['categoria'], steps=obj['steps'])
        
        with current_app.app_context():
            db.session.add(newReceita)
            db.session.commit()

        for x in obj['ingredientes']:
            ingrediente_recipe =  IngReceitaModel(id_receita=recipe.id, id_ing=x['id_ingrediente'], qtd=x['quantidade'] )

        with current_app.app_context():
            db.session.add(ingrediente_recipe)
            db.session.commit() 

        res = json.dumps({'id': _id})
        return Response(res, mimetype='application/json', status=200)

    except SQLAlchemyError as error:
        res = json.dumps({"Erro": str(error.__dict__['orig'])})
        return Response(res, mimetype='application/json', status=500)
    
    except Exception as error:
        res = json.dumps({"Erro": str(error)})
        return Response(res, mimetype='application/json', status=500)


@receitabp.route('/edit/<id>')
def get_recipe_by_id(id):
    recipes = get_recipes()
    recipe = find_recipe(recipes, id)
    return render_template('recipe/edit-recipe/edit-recipe.html', data={'recipe': recipe})


@receitabp.route('/pesquisa/<nome>')
def get_recipe_by_category(nome):
    recipes = get_recipes()
    recipe = find_recipecategory(recipes,nome)
    return render_template('recipe/recipe.html',title='Receitas', data={'recipes': recipe})


@receitabp.route('/getRecipes', methods=['GET'])
def get_recipes():
    try:
      

        allrecipe = ReceitaModel.query.all()

        return allrecipe
        
    except:
        db = SQLAlchemy(current_app)

        allrecipe = ReceitaModel.query.all()  
        return Response(res, mimetype='application/json', status=200)
    
  
def find_recipe(recipe_list, recipe_id):
    recipe_id = int(recipe_id)
    for recipe in recipe_list:
        if recipe['id'] == recipe_id:
            return recipe

def find_recipecategory(recipe_list, recipe_category):
    lista=[]
    for recipe in recipe_list: 
        if recipe['category'] == recipe_category:
            lista.append(recipe)
    return lista    
