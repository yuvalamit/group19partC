from flask import Blueprint

main_nav = Blueprint('main_nav', __name__, static_folder='static', static_url_path='/components/main_nav',
                     template_folder='templates')

