from core.db_wrapper import load_all_recipes
from search import RecipeSearch
import argparse
from cache import Cache

print("Start Gourmet Recipe Exporter v1")
# Abort program and print error in case if the customization isn't setup correctly
import hint_for_customizing
from customizing.custom_recipe_tags import init_tags
from customizing.custom_recipe_searches import queries

# Create all custom tags
init_tags()

parser = argparse.ArgumentParser(description='Gourmet Recipe Manager PDF Exporter')
parser.add_argument('-db_dir', action="store", dest="db_dir", required=True,
                    help='The path to the gourmet database file.')
parser.add_argument('-export_dir', action="store", dest="export_dir", required=True,
                    help='All recipes are exported to this folder.')
parser.add_argument('-include_images', action="store_true", default=False, help='Should exported recipes have images.')
parser.add_argument('-link_dir', action="store", dest="link_dir", default=None,
                    help='This path is used to set link to recipes from searches.')
parser.add_argument('-disable_cache', action="store_true", default=False,
                    help='If activated only modified recieps are written to disk')
parser.add_argument('-builder', action="store", dest="builder", default="", help='The repository owner of the recipe.')


program_options = parser.parse_args()
# Enable cache if needed
Cache.enabled = not program_options.disable_cache
# Print Options
print("Use cache: ", Cache.enabled)
print("Include Images: ", program_options.include_images)
print("Link dir: ", program_options.link_dir)
print("Export dir: ", program_options.export_dir)
print("Database path: ", program_options.db_dir)

# Load all recipes
recipes = load_all_recipes(program_options.db_dir)

options1 = {
    "export_folder": program_options.export_dir,
    "link_prefix": program_options.link_dir,
    "export_images": program_options.include_images,
    "builder": program_options.builder,
    "db_dir": program_options.db_dir,
}

# Write result
search1: RecipeSearch = RecipeSearch(recipes, queries, options1)
search1.create_pdfs()
