from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Receita(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    steps = db.Column(db.Integer, nullable=False)
    ingredients = db.Column(db.String(1000), nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())