from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class IngredienteReceita(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_ingrediente=db.Column(db.Integer, nullable=False)
    id_receita=db.Column(db.Integer,nullable=False)
    name = db.Column(db.String(50), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
