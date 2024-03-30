from flask import Blueprint, render_template, request, session, redirect
from utils.db_connector import *
from utils.session import session_logged_in
from bson.objectid import ObjectId

recipe = Blueprint('recipe', __name__, static_folder='static', static_url_path='/pages/recipe',
                   template_folder='templates')


@recipe.route('/recipe/<string:recipe_id>')
def get_recipe(recipe_id):
    recipe_doc = get_single_recipe_with_comments(recipe_id)
    return render_template('recipe.html', recipe=recipe_doc, LoggedIn=session_logged_in())


@recipe.route('/recipe/<string:recipe_id>', methods=['POST'])
def insert_comment(recipe_id):
    comment = request.form['comment']
    comment = {
        'recipe_id': ObjectId(recipe_id),
        'comment': comment,
        'user_id': ObjectId(session['userId']),
        'name': session['firstName'] + ' ' + session['lastName']
    }
    insert_comment_recipe(comment)
    return redirect('/recipe/' + recipe_id)
