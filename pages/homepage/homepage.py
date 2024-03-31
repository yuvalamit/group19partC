from flask import Blueprint, render_template, session, request

from utils.db_connector import *
from utils.session import session_logged_in

homepage = Blueprint('homepage', __name__, static_folder='static', static_url_path='/pages/homepage',
                     template_folder='templates')


@homepage.route('/')
def home_page():
    all_recipes = get_list_of_recipes()
    categories = get_categories()
    return render_template('homepage.html', all_recipes=all_recipes, LoggedIn=session_logged_in(),
                           categories=categories)


@homepage.route('/category/<string:category_name>')
def category_page(category_name):
    all_recipes = get_list_of_recipes(category_name)
    categories = get_categories()
    return render_template('homepage.html', all_recipes=all_recipes, LoggedIn=session_logged_in(),
                           categories=categories)
