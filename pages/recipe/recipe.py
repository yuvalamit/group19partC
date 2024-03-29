from flask import Blueprint, render_template
from utils.db_connector import *

recipe = Blueprint('recipe', __name__, static_folder='static', static_url_path='/pages/recipe',
                     template_folder='templates')


@recipe.route('/recipe/<string:recipe_id>')
def get_recipe(recipe_id):
    recipe_doc = get_single_recipe(recipe_id)
    return render_template('recipe.html', recipe=recipe_doc)
