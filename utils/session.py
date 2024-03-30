from flask import session
from utils.db_connector import *


def set_session(email):
    user = find_user(email)
    session['email'] = email
    session['userId'] = str(user['_id'])
    session['loggedIn'] = True
    session['firstName'] = user['firstName']
    session['lastName'] = user['lastName']


# check if the user is logged in or not
def session_logged_in():
    return session['loggedIn'] if 'loggedIn' in session else False
