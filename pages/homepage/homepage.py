from flask import Blueprint, render_template

from utils.db_connector import *

homepage = Blueprint('homepage', __name__, static_folder='static', static_url_path='/pages/homepage',
                     template_folder='templates')


@homepage.route('/')
def home_page():
    all_recipes = get_list_of_recipes()
    return render_template('homepage.html',all_recipes=all_recipes)
