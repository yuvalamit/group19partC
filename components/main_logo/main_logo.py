from flask import Blueprint

main_logo = Blueprint('main_logo', __name__, static_folder='static', static_url_path='/components/main_logo', template_folder='templates')
