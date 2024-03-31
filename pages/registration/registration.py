from flask import Blueprint, render_template, request, redirect
from utils.db_connector import *
from utils.session import set_session

registration = Blueprint('registration', __name__, static_folder='static', static_url_path='/pages/registration',
                         template_folder='templates')


@registration.route('/registration')
def get_registration():
    return render_template('registration.html')


@registration.route('/registration', methods=['POST'])
def post_register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        city = request.form['city']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        birthdate = request.form['birth_date']

        # check if the passwords are equal and also if there is not user with this email
        if password != confirm_password or find_user(
                email) or email is None or email == '' or password is None or password == '' or city is None or city == '' or first_name is None or first_name == '' or last_name is None or last_name == '' or birthdate is None or birthdate == '':
            return render_template('registration.html', error='invalid')

        user = {
            'email': email,
            'password': password,
            'city': city,
            'birth_date': birthdate,
            'firstName': first_name,
            'lastName': last_name
        }
        insert_user(user)  # insert new user to db
        set_session(email)  # set session to login the user
        return redirect('/myrecipes')
