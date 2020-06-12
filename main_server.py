import flask
from flask import request, jsonify
from flask_httpauth import HTTPTokenAuth
import argparse
from core.db_wrapper import load_all_recipes
from customizing.custom_recipe_tags import init_tags
from customizing.custom_recipe_searches import queries
from server.recipes_to_json import recipes_to_json
API_VERSION = 1
# Create all custom tags
init_tags()


parser = argparse.ArgumentParser(description='Gourmet Recipe Manager PDF Exporter')
parser.add_argument('-db_dir', action="store", dest="db_dir", required=True,
                    help='The path to the gourmet database file.')

program_options = parser.parse_args()
# Load all recipes
recipes = load_all_recipes(program_options.db_dir)
print(recipes_to_json(recipes[0]))

# Direct access of recipes with their ids
ids_to_recipes = {recipe.id():recipe for recipe in recipes}
print(recipes)

app = flask.Flask(__name__)
app.config["DEBUG"] = True
auth = HTTPTokenAuth(scheme='Bearer')
# Idee ich erstelle Autoriserung skeys
tokens = {
    "secret-token-1": "john",
    "secret-token-2": "susan"
}

@auth.verify_token
def verify_token(token):
    if token in tokens:
        return tokens[token]

@auth.get_user_roles
def get_user_roles(user):
    print(user)
    if user == "john":
        return ["admin","user"]
    return ["user"]


@app.route('/', methods=['GET'])
def root():
    return jsonify({"api-version": API_VERSION})


@app.route('/recipes', methods=['GET'])
@auth.login_required
# Return pairs of recipes and modified date
def get_all_recipes():
    allRecipes = []
    for r in recipes:
        allRecipes.append({"id": r.id(),"last-modified": r.last_modified()})
    return jsonify(allRecipes)

# TODO Add Parameter last_modified => get_all_recipes can be remove
# TODO fields: Only these fields are returned e.g id and title or image
@app.route('/search', methods=['POST'])
@auth.login_required
def search():
    print("Got search")
    content = request.json
    ids = content['ids']
    found_recipes = []
    for id in ids:
        if id in ids_to_recipes:
            found_recipes.append(recipes_to_json(ids_to_recipes[id]))
    return jsonify(found_recipes)



#Batch return
@app.route("/recipes/<id>")
def get_recipes_info(id):
    assert id == request.view_args['id']

# Use SSL for encrypting so we can send password and so on
app.run(ssl_context='adhoc')

# TODO Blueprints https://stackoverflow.com/questions/15231359/split-python-flask-app-into-multiple-files
# Die einzelen Methoden aufteilen
#### Wichtig nicht in ein Plu
# Endpunkte
# A. Rezepte änder abrufen
# B. Search auf bestimme Felder reduzieren
# C. Autorisierung (Admin,Read, Write)
# TODO Rezepte lösche sollte ein anderes level sein als z. B favorit Rezpe ändern
# E. Rezepte in PDFs umwandeln und abrufen
# F. Statiskten
# Abrufen
# Ändern
# G: Benutzer Endpunkt
# Berechtigungen und lsit abrufen
# Passwort ändern



