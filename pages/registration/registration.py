from flask import Blueprint, render_template

registration = Blueprint('registration', __name__, static_folder='static', static_url_path='/pages/registration',
                     template_folder='templates')


@registration.route('/registration')
def get_registration():
    return render_template('registration.html')
