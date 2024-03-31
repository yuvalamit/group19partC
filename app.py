from flask import Flask
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

## Pages
## Home Page
from pages.homepage.homepage import homepage

app.register_blueprint(homepage)

from pages.registration.registration import registration

app.register_blueprint(registration)

from pages.login.login import login

app.register_blueprint(login)

from pages.myrecipes.myrecipes import myrecipes

app.register_blueprint(myrecipes)

from pages.recipe.recipe import recipe

app.register_blueprint(recipe)

from pages.upload.upload import upload

app.register_blueprint(upload)
## End Pages

## Components

from components.main_nav.main_nav import main_nav

app.register_blueprint(main_nav)

from components.main_logo.main_logo import main_logo

app.register_blueprint(main_logo)

## End Components

if __name__ == "__main__":
    app.run(debug=True)
