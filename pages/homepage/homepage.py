from flask import Blueprint, render_template

homepage = Blueprint('homepage', __name__, static_folder='static', static_url_path='/pages/homepage',
                     template_folder='templates')


@homepage.route('/')
def home_page():
    return render_template('homepage.html')
