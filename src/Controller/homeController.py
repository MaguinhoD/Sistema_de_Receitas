import json
from flask import Blueprint, current_app, render_template,request,Response,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError


homeBp = Blueprint('home',__name__, url_prefix='/home')



@homeBp.route('/main')
def main():
    return render_template('Home/home.html', title='Home')