import json
from flask import Blueprint, current_app, render_template,request,Response,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError


from src.Model.receitaModel import Receita as ReceitaModel
from src.Model.IngredientedaReceitaModel import IngredienteReceita as IngredienteReceitaModel
from src.Model.IngredienteModel import Ingrediente as IngredienteModel

receitasBp = Blueprint('receitas',__name__, url_prefix='/receitas')


@receitasBp.route('/main')
def main():
    return render_template('Receitas/receitas.html', title='receitas')

@receitasBp.route('/bolo')
def bolo():
    
    try:


        db = SQLAlchemy(current_app)
        receitas= ReceitaModel.query.filter_by(category='bolo')
        return render_template('Receitas/receitas.html', title='bolo')
        

    except SQLAlchemyError as error:
        res = json.dumps({"Erro": str(error.__dict__['orig'])})
        return Response(res, mimetype='application/json', status=500)

    except Exception as error:
        res = json.dumps({"Erro": str(error)})
        return Response(res, mimetype='application/json', status=500)


@receitasBp.route('/register')
def register():
    return render_template('Register/register.html', title='Cadastre-se')

@receitasBp.route('/verReceita', methods=["POST","GET"])
def getRecetia():
    return #ver receita

    
@receitasBp.route('/cadastrarReceita', methods=["POST","GET"])
def registrarReceita():
    return render_template('CadastrarReceita/cadastrar.html', title='Crie uma Receita')


@receitasBp.route('/addReceita', methods=["POST","GET"])
def addReceita():
    try:
        db = SQLAlchemy(current_app)
        
        obj = request.json
        newReceita= ReceitaModel(**obj)

        with current_app.app_context():
            db.session.add(newReceita)
            db.session.commit()

        _id = ReceitaModel.query.filter_by(name=request.form['nome']).first().id

        res = json.dumps({'id': _id})
        return Response(res, mimetype='application/json', status=200)

    except SQLAlchemyError as error:
        res = json.dumps({"Erro": str(error.__dict__['orig'])})
        return Response(res, mimetype='application/json', status=500)
    
    except Exception as error:
        res = json.dumps({"Erro": str(error)})
        return Response(res, mimetype='application/json', status=500)


@receitasBp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    ingrediente = Ingrediente.query.get(id)
    if  request.method == "POST":
        ingrediente.nome = request.form['nome']
        ingrediente.qtd = request.form["qtd"]
        db.session.commit()
        return redirect(url_for("CRUD"))
    return render_template("edit.html", ingrediente=ingrediente)

@receitasBp.route("/delete/<int:id>")
def delete(id):
    ingrediente = Ingrediente.query.get(id)
    db.session.delete(ingrediente)
    db.session.commit()       
    return redirect(url_for("CRUD"))

@receitasBp.route("/add", methods=["POST","GET"])
def add():
    try:
        db = SQLAlchemy(current_app)
        obj = request.json
        newIngrediente = IngredienteModel(name=obj['name'])    
        newIngredienteReceita = IngredienteReceitaModel({'id_ingrediente':newIngrediente.id,**obj})    
        with current_app.app_context():
                db.session.add(newIngrediente)
                db.session.add(newIngredienteReceita)
                db.session.commit()       


        _id = IngredienteReceitaModel.query.filter_by(name=obj['nome']).first().id

        res = json.dumps({'id': _id})
        return Response(res, mimetype='application/json', status=200)

    except SQLAlchemyError as error:
        res = json.dumps({"Erro": str(error.__dict__['orig'])})
        return Response(res, mimetype='application/json', status=500)
    
    except Exception as error:
        res = json.dumps({"Erro": str(error)})
        return Response(res, mimetype='application/json', status=500)
        