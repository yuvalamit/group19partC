from flask import Blueprint, render_template, session, redirect, url_for

myrecipes = Blueprint('myrecipes', __name__, static_folder='static', static_url_path='/pages/myrecipes',
                     template_folder='templates')


@myrecipes.route('/myrecipes')
def get_myrecipes():
    if 'loggedIn' in session and session['loggedIn']:
        email = session.get('email')
        user_id = session.get('userId')
        first_name = session.get('firstName')
        return render_template('myrecipes.html', first_name=first_name, LoggedIn=session['loggedIn'])
    else:
        return redirect(url_for('login'))
