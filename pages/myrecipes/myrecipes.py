from flask import Blueprint, render_template, session, redirect, url_for

from utils.db_connector import get_user_recipes
from utils.session import session_logged_in

myrecipes = Blueprint('myrecipes', __name__, static_folder='static', static_url_path='/pages/myrecipes',
                      template_folder='templates')


@myrecipes.route('/myrecipes')
def get_myrecipes():
    if session_logged_in():
        user_id = session.get('userId')
        first_name = session.get('firstName')
        recipes = get_user_recipes(user_id)
        return render_template('myrecipes.html', recipes=recipes, first_name=first_name, LoggedIn=session['loggedIn'])
    else:
        return redirect('/login')
