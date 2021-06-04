<<<<<<< HEAD
from flask import Blueprint, render_template, request
from flask.helpers import url_for
=======
import json

from flask import Blueprint, render_template, request, current_app, Response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
>>>>>>> entrega_2

ingredientebp = Blueprint('ingrediente', __name__, url_prefix='/ingredientes')

from src.Model.receitaModel import Ingrediente as ingredienteModel

@ingredientebp.route('/', methods=['GET'])
def index():
    try:
        ingredients = get_ingredients()
    except Exception as error:
        print(error)
        ingredients = []
    return render_template('ingredient/ingredient.html', title='Ingredientes', data={'ingredients': ingredients})


def get_ingredients():
    try:
        db = SQLAlchemy(current_app)
        ingredients = ingredienteModel.query.all()
        if not ingredients:
            raise Exception('Nenhum ingrediente')

              
        return ingredients

    
    
    except Exception as error:
        res = json.dumps({"Erro": str(error)})
        return None    


@ingredientebp.route('/create', methods=['GET', 'POST'])
def create_ingredients():
    if request.json:
        try:
            db = SQLAlchemy(current_app)
            obj = request.json

        
            ingredient = ingredienteModel(**obj)
           
            with current_app.app_context():
                db.session.add(ingredient)
                db.session.commit()

            res = json.dumps({'message': 'Ingrediente cadastrado!', 'error': False})
            return Response(res, mimetype='application/json', status=200)

        

        except Exception as error:
            res = json.dumps({'message': str(error), 'error': True})
            
            return Response(res, mimetype='application/json', status=500)
    else:
        try:
            ingredients = get_ingredients()
        except Exception as error:
            print(error)
            ingredients = []
        return render_template('ingredient/create-ingredient/create-ingredient.html', title='Adicionar ingredientes',data={'ingredients': ingredients})


@ingredientebp.route('/edit/<_id>', methods=['GET', 'PUT'])
def update_ingredient(_id):
    if request.json:
        try:
            db = SQLAlchemy(current_app)
            obj = request.json

            ingredient = ingredienteModel.query.filter_by(id=_id).first()
            ingredient.name = obj['name']

            with current_app.app_context():
                db.session.merge(ingredient)
                db.session.commit()

            res = json.dumps({'message': 'Ingrediente atualizado com sucesso', 'error': False})
            return Response(res, mimetype='application/json', status=200)
        except Exception as error:
            res = json.dumps({'message': str(error), 'error': True})
            return Response(res, mimetype='application/json', status=500)
    else:
        ingredient = ingredienteModel.query.filter_by(id=_id).first()
        return render_template('ingredient/edit-ingredient/edit-ingredient.html', title='Editar ingrediente', ingredient=ingredient)


@ingredientebp.route('/delete/<_id>', methods=['DELETE'])
def delete_ingredient(_id):
    try:
        db = SQLAlchemy(current_app)

        with current_app.app_context():
            db.session.query(ingredienteModel).filter_by(id=_id).delete()
            db.session.commit()

        res = json.dumps({'message': 'Ingrediente excluído', 'error': False})
        return Response(res, mimetype='application/json', status=200)

    except Exception as error:
        res = json.dumps({'message': str(error), 'error': True})
        return Response(res, mimetype='application/json', status=500)
