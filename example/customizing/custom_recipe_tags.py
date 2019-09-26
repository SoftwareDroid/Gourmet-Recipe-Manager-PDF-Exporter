from core.tags import RecipeTag, register_tag, all_tags

all_tags = {}

def init_tags():
    # We don't want call this method twice
    if len(all_tags) != 0:
        return
    # name: str, display_name:str,render_priority: int, color: str,render: bool
    register_tag(RecipeTag("vegetarian", "Vegetarian", 30, "green darken-4", True))
    register_tag(RecipeTag("vegan", "Vegan", 25, "light-green", True))
    register_tag(RecipeTag("experiment", "Experiment", 20, "purple accent-3", True))
    register_tag(RecipeTag("todo", "TODO", 15, "teal", True))
    register_tag(RecipeTag("favorite", "Favorite", 10, "cyan accent-4", True))
    register_tag(RecipeTag("grill", "Need Grill", 10, "red darken-4", True))


