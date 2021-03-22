import json
from flask import Blueprint, current_app, render_template,request,Response,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError


from src.Model.receitaModel import Receita as ReceitaModel

pesquisarBp = Blueprint('pesquisar',__name__, url_prefix='/pesquisar')

@pesquisarBp.route('/bolo')
def bolo():
    return render_template('Receitas/receitas.html', title='receitas')
    try:


        db = SQLAlchemy(current_app)
        obj=request.json
        receitas= receitaModel.query.filter_by(category=obj['category'])

        

    except SQLAlchemyError as error:
        res = json.dumps({"Erro": str(error.__dict__['orig'])})
        return Response(res, mimetype='application/json', status=500)

    except Exception as error:
        res = json.dumps({"Erro": str(error)})
        return Response(res, mimetype='application/json', status=500)


@pesquisarBp.route('/register')
def register():
    return render_template('Register/register.html', title='Cadastre-se')

@pesquisarBp.route('/verReceita', methods=["POST","GET"])
def getRecetia():
    return #ver receita

    
@pesquisarBp.route('/registrarReceita', methods=["POST","GET"])
def registrarReceita():
    try:

        db = SQLAlchemy(current_app)

        obj=request.json
        newUser=UserModel(**obj)

        with current_app.app_context():
            db.session.add(newUser)
            db.session.commit()

        _id = UserModel.query.filter_by(email=obj['email']).first().id

        res = json.dumps({'id':_id})
        return Response(res,mimetype='application/json',status=200)

    except SQLAlchemyError as error:
        res = json.dumps({"Erro": str(error.__dict__['orig'])})
        return Response(res, mimetype='application/json', status=500)

    except Exception as error:
        res = json.dumps({"Erro": str(error)})
        return Response(res, mimetype='application/json', status=500)


