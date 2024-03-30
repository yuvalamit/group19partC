from dotenv import load_dotenv

load_dotenv()
from utils.db_connector import users_col, categories_col, recipes_col, comments_col

print('DB DATA:')
users = users_col.find()
print('Users:')
for user in users:
    print(user)

print()

categories = categories_col.find()
print('Categories:')
for category in categories:
    print(category)

print()

recipes = recipes_col.find()
print('Recipes:')
for recipe in recipes:
    print(recipe)

print()

comments = comments_col.find()
print('Comments:')
for comment in comments:
    print(comment)
