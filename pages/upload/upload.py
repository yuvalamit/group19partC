from flask import Blueprint, render_template

upload = Blueprint('upload', __name__, static_folder='static', static_url_path='/pages/upload',
                     template_folder='templates')


@upload.route('/upload')
def get_upload():
    return render_template('upload.html')
