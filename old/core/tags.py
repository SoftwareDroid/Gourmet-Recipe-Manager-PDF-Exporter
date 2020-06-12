import re

_valid_recipe_name_patter = re.compile("[0-9a-zA-Z_]+")


class RecipeTag:
    def __init__(self, name: str, display_name: str, render_priority: int, color: str, render: bool):
        self._name = name
        self._display_name = display_name
        self._color = color
        self._render = render
        self._render_prio = render_priority

    def display_name(self):
        return self._display_name

    def render_priority(self):
        return self._render_prio

    def name(self):
        return self._name

    def color(self):
        # See https://github.com/taketwo/glasbey
        return self._color

    def render(self):
        return self._render


# A dict which contains all custom tags
all_tags = {}


def register_tag(tag: RecipeTag):
    if not _valid_recipe_name_patter.match(tag.name()):
        print(tag.name(), " doesn't match the pattern for custom tags")
        return
    assert tag.name() not in all_tags, "Keyword already used"
    all_tags[tag.name()] = tag
