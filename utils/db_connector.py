import os
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId

# get your uri from .env file
uri = os.environ.get('DB_URI')

# create cluster
cluster = MongoClient(uri, server_api=ServerApi('1'))

# get all dbs and collections that needed
mydatabase = cluster['foodbook_db']
users_col = mydatabase['users']
recipes_col = mydatabase['recipes']
categories_col = mydatabase['categories']
comments_col = mydatabase['comments']


# recipes functions
def get_list_of_recipes(category_name=None):
    if category_name:
        category = find_category_by_name(category_name)
        if category:
            category_id = ObjectId(category['_id'])
            return list(recipes_col.find({
                '$or': [
                    {'category1': category_id},
                    {'category2': category_id},
                    {'category3': category_id}
                ]
            }))
    return list(recipes_col.find())


def insert_comment_recipe(comment):
    return comments_col.insert_one(comment)


def get_user_recipes(user_id):
    return list(recipes_col.find({'uploaded_by': ObjectId(user_id)}))


def insert_recipe(recipe):
    return recipes_col.insert_one(recipe)


def get_single_recipe_with_comments(recipe_id):
    recipe = recipes_col.find_one({'_id': ObjectId(recipe_id)})
    if recipe:
        # Get all comments for the recipe from the comments collection
        recipe_comments = comments_col.find({'recipe_id': ObjectId(recipe_id)})
        # Add the comments to the recipe document
        recipe['comments'] = list(recipe_comments)
    return recipe


# end - recipes functions

# user functions
def find_user(email):
    return users_col.find_one({'email': email})


def insert_user(user):
    return users_col.insert_one(user)


# end - user functions

# categories functions
def get_categories():
    return list(categories_col.find())


def find_category(category_id):
    return categories_col.find_one({'_id': ObjectId(category_id)})


def find_category_by_name(category_name):
    return categories_col.find_one({'name': category_name})
# end - categories functions
