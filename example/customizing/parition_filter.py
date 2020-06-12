from core import Recipe

def only_tag(tag :str):
    def _filter(recipe: Recipe):
        if recipe.has_tag(tag):
            return tag
        else:
            None
    return _filter

def partition_after_tag(tag: str):
    def _filter(recipe: Recipe):
        if recipe.has_tag(tag):
            return tag + " is set"
        else:
            return tag + " not set"
    return _filter

def time_partition(recipe: Recipe):
    prep_time: float = recipe._preptime
    cook_time: float = recipe._cooktime
    total_time_in_hours: float = (prep_time + cook_time) / (60.0**2)
    if recipe.has_unknown_cooktime():
        return "Z. Unknown cooking time"
    if total_time_in_hours < 1.0:
        return "A. Recipes < 1 h"
    elif total_time_in_hours <= 1.5:
        return "B. Recipes < 1.5 h"
    elif total_time_in_hours <= 2:
        return "C. Recipes < 2 h"
    elif total_time_in_hours <= 2.5:
        return "D. Recipes < 2.5 h"
    elif total_time_in_hours <= 3:
        return "E. Recipes < 3 h"
    else:
        return "F. Recipes < 3 h"