from flask_sqlalchemy import SQLAlchemy

from src.Model.ingredienteModel import Ingrediente

db = SQLAlchemy()



ingrediente_receita = db.Table('ingrediente_receita',
    db.Column('rec_id',db.Integer,db.ForeignKey('receita.rec_id')),
    db.Column('ing_id', db.Integer, db.ForeignKey(Ingrediente.ing_id)),
    db.Column('qtd',db.String()))



class Receita(db.Model):
    __tablename__ = 'receita'

    rec_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50),nullable=False)
    steps = db.Column(db.Integer, nullable=False)
    ingredients = db.relationship(Ingrediente, secondary=ingrediente_receita, lazy='subquery', backref=db.backref('receita', lazy=True))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())



    def __init__(self,nome,steps):
        self.nome = nome
        self.steps = steps

    def __repr__(self):
        return '{}'.format(self.name)


    def serialize(self):
        return{
            'id':self.id, 'name': self.name, 'steps':self.steps
        }


