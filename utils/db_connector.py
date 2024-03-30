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


# recipes functions
def get_list_of_recipes():
    return list(recipes_col.find())


def get_single_recipe(recipe_id):
    return recipes_col.find_one({'_id': ObjectId(recipe_id)})


# end - recipes functions

# user functions
def find_user(email):
    return users_col.find_one({'email': email})
# end - user functions
