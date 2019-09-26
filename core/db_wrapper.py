
from typing import Sequence
from core.recipe import Recipe, Ingredient


def load_all_recipes(db_dir: str) -> Sequence[Recipe]:
    """Fetch all recipes from the database"""
    import sqlite3
    def get_all_ingredients(c, id) -> Sequence[Ingredient]:
        t = (id,)
        c.execute('SELECT * FROM ingredients WHERE recipe_id=?', t)
        ingredients = []
        for row in c.fetchall():
            ingredient = Ingredient(refid=row[2], unit=row[3], amount=row[4], rangeamount=row[5], item=row[6],
                                    optional=row[8], inggroup=row[10],position= row[11],deleted=row[12])
            ingredients.append(ingredient)
        return ingredients

    conn = sqlite3.connect(db_dir)
    c = conn.cursor()
    c2 = conn.cursor()
    # Retrieve all recipes
    c.execute('SELECT * FROM recipe')
    recipes = []
    for row in c.fetchall():
        recipe = Recipe(id=row[0], title=row[1], instructions=row[2], notes=row[3], cuisine=row[4], rating=row[5],
                        description=row[6],
                        source=row[7], preptime=row[8], cooktime=row[9], servings=row[10], yields=row[11],
                        yield_unit=row[12], image=row[13],
                        thumb=row[14], deleted=row[15], link=row[18], last_modified=row[19])
        recipe._obj_ingredients = get_all_ingredients(c2, recipe.id())
        recipes.append(recipe)
    conn.close()
    return recipes


