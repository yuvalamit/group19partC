from bson import ObjectId
from flask import Blueprint, render_template, request, redirect, session
from utils.db_connector import get_categories, insert_recipe
from utils.session import session_logged_in
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static', 'media')

upload = Blueprint('upload', __name__, static_folder='static', static_url_path='/pages/upload',
                   template_folder='templates')


@upload.route('/upload')
def get_upload():
    categories = get_categories()
    return render_template('upload.html', LoggedIn=session_logged_in(), categories=categories)


@upload.route('/upload', methods=['POST'])
def post_upload():
    if request.method == 'POST':
        name = request.form['name']
        ingredients = request.form['ingredients'].split('\n')
        instructions = request.form['instructions']
        hardness = request.form['hardness']
        minutes = request.form['minutes']
        kosher = request.form.get('kosher') == 'on'  # checkbox
        category1 = ObjectId(request.form['category1'])
        category2 = ObjectId(request.form['category2'])
        category3 = ObjectId(request.form['category3'])
        print('until here')
        # saving file in system
        photo = request.files['photo']
        filename = secure_filename(photo.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        photo.save(filepath)

        recipe = {
            'name': name,
            'ingredients': ingredients,
            'instructions': instructions,
            'hardness': hardness,
            'minutes': minutes,
            'kosher': kosher,
            'category1': category1,
            'category2': category2,
            'category3': category3,
            'uploaded_by': ObjectId(session.get('userId')),
            'image': filename,
        }
        insert_recipe(recipe)  # insert new user to db
        return redirect('/myrecipes')
