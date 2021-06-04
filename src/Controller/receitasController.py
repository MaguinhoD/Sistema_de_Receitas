import json
from flask import Blueprint, current_app, render_template,request,Response,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError



from src.Controller.ingredientesController import get_ingredients
from src.Model.receitaModel import Receita as ReceitaModel
from src.Model.receitaModel import ingrediente_receita as IngReceitaModel
from src.Model.receitaModel import Ingrediente as ingredienteModel

receitabp = Blueprint('receita', __name__, url_prefix='/receitas')


@receitabp.route('/', methods=['GET'])
def index():
    recipes = get_recipes()
    return render_template('recipe/recipe.html', title='Receitas', data={'recipes': recipes})


def get_recipes():
    try:
        db = SQLAlchemy(current_app)

        recipes = ReceitaModel.query.all()
        if not recipes:
            return norecipe()
    
        
        return recipes

    except Exception as error:
        res = json.dumps([])
        print(error)
        raise Exception('ERROR')

@receitabp.route('/criarreceita', methods=[ 'POST','GET'])
def criarreceita():
        try:
            ingredients = get_ingredients()
        except Exception as error:
            print(error)
            ingredients = []
        return render_template('recipe/create-recipe/create-recipe.html',data={'ingredients': ingredients})



@receitabp.route('/createrecipe', methods=['POST', 'GET'])
def createrecipe():
    try:

            db = SQLAlchemy(current_app)

            obj = request.json
            ingid=[]
            name = obj['name']
            steps = obj['steps']
            category = obj['category']
            for x in obj['ingrediente']:
                ingid.append(x['id'])

            ingredientes = list(map(lambda x: ingredienteModel.query.filter_by(id=x).first(), ingid))
            
            newReceita = ReceitaModel(name=name,category=category ,steps=steps,ingredientes=ingredientes)
            
            with current_app.app_context():
                current_db_sessions = db.object_session(newReceita)
                current_db_sessions.add(newReceita)
                current_db_sessions.commit()
                

                       
            res = json.dumps({'message': 'Receita cadastrada!', 'error': False})
            return Response(res, mimetype='application/json', status=200)

    except Exception as error:
            res = json.dumps({'message': str(error), 'error': True})
            return Response(res, mimetype='application/json', status=200)

@receitabp.route('/edit/<_id>',methods=['POST','PUT','GET'])
def get_recipe_by_id(_id):
        ingredients = get_ingredients()
        recipe = ReceitaModel.query.filter_by(id=_id).first()
        return render_template('recipe/edit-recipe/edit-recipe.html', data={'ingredients': ingredients,'recipe':recipe})

@receitabp.route('/edit/<_id>',methods=['POST','GET','PUT'])
def editrecipe(_id):
    
         try:
            db = SQLAlchemy(current_app)
            obj = request.json
            ingid=[]
            receita = ReceitaModel.query.filter_by(id=_id).first()

            receita.name=obj['name']
            receita.category=obj['category']
            receita.steps=obj['steps']
            for x in obj['ingrediente']:
                ingid.append(x['id'])

            receita.ingredientes = list(map(lambda x: ingredienteModel.query.filter_by(id=x).first(), ingid))

            with current_app.app_context():
                db.session.merge(receita)
                db.session.commit()

            

            res = json.dumps({'message': 'Ingrediente atualizado com sucesso', 'error': False})
            return Response(res, mimetype='application/json', status=200)

         except Exception as error:
            res = json.dumps({'message': str(error), 'error': True})
            return Response(res, mimetype='application/json', status=500)

 

    
@receitabp.route('/pesquisa/<nome>')
def get_recipe_by_category(nome):
    recipes = ReceitaModel.query.filter_by(category=nome)
    
    return render_template('recipe/recipe.html',title='Receitas', data={'recipes': recipes})



  
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


@receitabp.route('/delete/<_id>', methods=['DELETE'])
def delete_receita(_id):
    try:
        db = SQLAlchemy(current_app)

        with current_app.app_context():
            db.session.query(ReceitaModel).filter_by(id=_id).delete()
            db.session.commit()

        res = json.dumps({'message': 'Ingrediente excluído', 'error': False})
        return Response(res, mimetype='application/json', status=200)

    except Exception as error:
        res = json.dumps({'message': str(error), 'error': True})
        return Response(res, mimetype='application/json', status=500)

def norecipe():
    return {
            'id': 0,
            'name': 'Nenhuma Receita Cadastrada',
            'category':' ',
            'ingredients': {
                ' ': ' '
            },
            'steps': ' ',
            'created-at': ' '
        },