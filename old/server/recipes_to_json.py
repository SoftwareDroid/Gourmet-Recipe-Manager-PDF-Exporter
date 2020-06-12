from old.core.recipe import Recipe

def recipes_to_json(recipe: Recipe):
    return {"id": recipe.id(),
            "title": recipe.title(),
            "rating": recipe.rating(),
            "link": recipe.link(),
            "source": recipe.source(),
            "cooktime": recipe.cooktime(),
            "cuisine": recipe.cuisine(),
            }