from flask import Blueprint, render_template, request
from flask.helpers import url_for

ingredientebp = Blueprint('ingrediente', __name__, url_prefix='/ingredientes')


@ingredientebp.route('/')
def index():
    ingredients = get_ingredients()
    return render_template('ingredient/ingredient.html', title='Ingredientes', data={'ingredients': ingredients})


@ingredientebp.route('/create', methods=['GET', 'POST'])
def create_ingredients():
    if request.method == 'POST':
        ingredients = Ingrediente(request.form.get('ingredients'))
        db.session.add(ingredients)
        db.session.commit()
        return redirect(url_for("ingredients"))
        
    return render_template('ingredient/create-ingredient/create-ingredient.html', title='Adicionar ingredientes')


@ingredientebp.route('/edit', methods=['GET', 'PUT'])
def update_ingredients():
    stored_ingredients = get_ingredients()
    if request.method == 'PUT':
        ingredients = request.form.get('ingredients')
    return render_template('ingredient/edit-ingredient/edit-ingredient.html', title='Editar ingredientes',
                           data={'ingredients': stored_ingredients})


@ingredientebp.route('/getIngredients')
def get_ingredients():
    return [
        {
            'id': 1,
            'name': 'Trigo',
            'created_at': '10/03/2021'
        },
        {
            'id': 2,
            'name': 'Ovo',
            'created_at': '10/03/2021'
        },
        {
            'id': 3,
            'name': 'Leite',
            'created_at': '10/03/2021'
        },
        {
            'id': 4,
            'name': 'Fermento em pó',
            'created_at': '10/03/2021'
        },
        {
            'id': 5,
            'name': 'Chocolate em pó',
            'created_at': '10/03/2021'
        },
        {
            'id': 6,
            'name': 'Milho',
            'created_at': '10/03/2021'
        },
        {
            'id': 7,
            'name': 'Óleo',
            'created_at': '10/03/2021'
        },
        {
            'id': 8,
            'name': 'Peixe',
            'created_at': '10/03/2021'
        }


    ]
