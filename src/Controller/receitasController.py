import json
from flask import Blueprint, current_app, render_template,request,Response,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError



from src.Controller.ingredientesController import get_ingredients


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

    stored_ingredients = get_ingredients()
    return render_template('recipe/create-recipe/create-recipe.html', data={'stored_ingredients': stored_ingredients})


@receitabp.route('/edit/<id>')
def get_recipe_by_id(id):
    recipes = get_recipes()
    recipe = find_recipe(recipes, id)
    return render_template('recipe/edit-recipe/edit-recipe.html', data={'recipe': recipe})


@receitabp.route('/pesquisa/<string>')
def get_recipe_by_category(a):
    recipes = get_recipes()
    recipe = find_recipecategory(recipes,a)
    return render_template('recipe/edit-recipe/edit-recipe.html', data={'recipe': recipe})


@receitabp.route('/getRecipes', methods=['GET'])
def get_recipes():
    return [
        {
            'id': 1,
            'name': 'Bolo de fubá',
            'category':'Bolo',
            'ingredients': {
                'Trigo': '3 xícaras',
                'Ovo': '3 xícaras',
                'Oléo': '1 xícara',
                'Fubá': '1 xícara'
            },
            'steps': '1 - Misturar os ingredientes, 2 - Bater a massa, 3- Assar',
            'created-at': '10/03/2021'
        },
        {
            'id': 2,
            'name': 'Bolo de chocolate',
            'category':'Bolo',
            'ingredients': {
                'Trigo': '3 xícaras',
                'Ovo': '3 xícaras',
                'Oléo': '1 xícara',
                'Chocolate': '1 xícara',
            },
            'steps': '1 - Misturar os ingredientes, 2 - Bater a massa, 3- Assar',
            'created-at': '10/03/2021'
        },
        {
            'id': 3,
            'name': 'Peixe ensopado',
            'category':'Frutos do Mar',
            'ingredients': {
                'Peixe':'2kg'
            },
            'steps': '1 - Cozinhar o peixe, 2 - Colocar os ingredientes',
            'created-at': '10/03/2021'
        }
       
    ]


def find_recipe(recipe_list, recipe_id):
    recipe_id = int(recipe_id)
    for recipe in recipe_list:
        if recipe['id'] == recipe_id:
            return recipe

def find_recipecategory(recipe_list, recipe_category):
    
    for recipe in recipe_list:
        if recipe['category'] == recipe_category:
            return recipe
