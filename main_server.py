import flask
from flask import request, jsonify
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

@app.route('/', methods=['GET'])
def root():
    return jsonify({"api-version": API_VERSION})



@app.route('/recipes', methods=['GET'])
# Return pairs of recipes and modified date
def get_all_recipes():
    allRecipes = []
    for r in recipes:
        allRecipes.append({"id": r.id(),"last-modified": r.last_modified()})
    return jsonify(allRecipes)


@app.route('/search', methods=['POST'])
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


app.run()

# Alle Rezepte Abrufen
# Einzelens Rezept Abrufen
# Rezept Nach PDF Konverieren

# Permission Lese Berechtigung, Schreib Berechtigung, Admin Berechtigung (Berechtigungen der anderen ändern)
# Benutzter Verwalten: Name, Password, Berechtigungslevel (Read, Write, Admin)



