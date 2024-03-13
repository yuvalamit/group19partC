from flask import Flask


app = Flask(__name__)

## Pages
## Home Page
from pages.homepage.homepage import homepage

app.register_blueprint(homepage)

from pages.registration.registration import registration

app.register_blueprint(registration)
## End Pages

## Components

from components.main_nav.main_nav import main_nav
app.register_blueprint(main_nav)

from components.main_logo.main_logo import main_logo
app.register_blueprint(main_logo)

## End Components

if __name__ == "__main__":
    app.run(debug=True)
