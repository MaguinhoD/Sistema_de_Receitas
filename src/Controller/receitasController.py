import json
from flask import Blueprint, current_app, render_template,request,Response,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError


from src.Model.receitaModel import Receita as ReceitaModel
from src.Model.IngredientedaReceitaModel import IngredienteReceita as IngredienteReceitaModel

receitasBp = Blueprint('receitas',__name__, url_prefix='/receitas')

@receitasBp.route('/bolo')
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


@receitasBp.route('/register')
def register():
    return render_template('Register/register.html', title='Cadastre-se')

@receitasBp.route('/verReceita', methods=["POST","GET"])
def getRecetia():
    return #ver receita

    
@receitasBp.route('/cadastrarReceita', methods=["POST","GET"])
def registrarReceita():
    return render_template('CadastrarReceita/cadastrar.html', title='Cadastre uma receita')






@receitasBp.route("/add", methods=["GET","POST"])
def add():
    db = SQLAlchemy(current_app)
    if request.method == "POST":
        

        db.session.add({'name':request.form['nome'],'quantidade': request.form['qtd']})
        db.session.commit()       
        return redirect(url_for("receitas"))
#    return render_template("add.html")

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
