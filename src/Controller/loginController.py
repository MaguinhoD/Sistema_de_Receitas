import json
from flask import Blueprint, current_app, render_template,request,Response,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError


from src.Model.usuarioModel import Usuario as UserModel

loginBp = Blueprint('account',__name__, url_prefix='/account')

@loginBp.route('/login')
def login():
    return render_template('Login/login.html', title='Login')

@loginBp.route('/register')
def register():
    return render_template('Register/register.html', title='Cadastre-se')

@loginBp.route('/getUsuario', methods=["POST","GET"])
def getUsuario():
    try:


        db = SQLAlchemy(current_app)
        obj=request.json
        user= UserModel.query.filter_by(email=obj['email']).first()

        if not user:
            raise Exception('Não foi encontrado usuário com esse e-mail')

        if user.password != obj['password']:
            raise Exception(' Senha Incorreta, tente novamente')

        res = json.dumps({'id': user.id, 'name':user.name, 'email':user.email})
        return Response(res, mimetype='application/json', status=200)

    except SQLAlchemyError as error:
        res = json.dumps({"Erro": str(error.__dict__['orig'])})
        return Response(res, mimetype='application/json', status=500)

    except Exception as error:
        res = json.dumps({"Erro": str(error)})
        return Response(res, mimetype='application/json', status=500)

@loginBp.route('/registerUser', methods=["POST","GET"])
def registerUser():
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


