from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()




class Ingrediente(db.Model):
    __tablename__ = 'ingrediente'

    ing_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())



    def __init__(self,name):
        self.name = name


    def __repr__(self):
        return '{}'.format(self.name)

    def serialize(self):
        return{
            'id':self.id, 'name':self.name
        }