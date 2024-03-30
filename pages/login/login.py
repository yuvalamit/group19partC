from flask import Blueprint, render_template, request, session, redirect
from utils.db_connector import *
from utils.session import set_session

login = Blueprint('login', __name__, static_folder='static', static_url_path='/pages/login',
                  template_folder='templates')


@login.route('/login')
def get_login():
    return render_template('login.html')


@login.route('/logout')
def logout():
    session.pop('email', None)
    session.pop('user_id', None)
    session.pop('loggedIn', False)
    session.pop('firstName', None)
    return redirect('/login')


@login.route('/login', methods=['POST'])
def post_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = find_user(email)
        if not user or user['password'] != password:
            # error login
            return render_template('login.html', error='invalid')
        # login success
        set_session(email)
        return redirect('/myrecipes')
