from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



ingrediente_receita=db.Table('ingrediente_receita',   
    db.Column('rec_id',db.Integer,db.ForeignKey('receita.id'),primary_key=True),
    db.Column('ing_id', db.Integer, db.ForeignKey('ingrediente.id'),primary_key=True),
    db.Column('qtd',db.Integer))
 



class Receita(db.Model):
    __tablename__ = 'receita'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50),nullable=False)
    steps = db.Column(db.String(1000), nullable=False)
    ingredientes = db.relationship('Ingrediente', secondary=ingrediente_receita, lazy='subquery', backref=db.backref('receita', cascade='all,delete', lazy=True))
    created_at = db.Column(db.DateTime, server_default=db.func.now())


    
    def __repr__(self):
        return '{}'.format(self.name)


    def serialize(self):
        return{
            'id':self.id, 'name': self.name, 'steps':self.steps, 'category':self.category
        }

class Ingrediente(db.Model):
    __tablename__ = 'ingrediente'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())



    def __repr__(self):
        return '{}'.format(self.name)

    def serialize(self):
        return{
            'id':self.id, 'name':self.name
        }


