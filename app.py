

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "hello"

from components.main_logo.main_logo import main_logo

app.register_blueprint(main_logo)