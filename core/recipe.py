from typing import Sequence, Optional
import base64
from humanfriendly import format_timespan
from core.tags import RecipeTag, all_tags
import re


class Ingredient:
    def __init__(self, refid: int, unit: str, amount: float, rangeamount: str, item: str, optional: int, deleted: int,
                 position: int, inggroup):
        self._unit = unit
        self._refid = refid
        self._amount = amount
        self._rangeamount = rangeamount
        self._item = item
        self._optional = optional
        self._deleted = deleted
        self._position = position
        self._inggroup = inggroup

    def __str__(self):
        return self.item()

    def inggroup(self):
        return self._inggroup

    def optional(self) -> int:
        return self._optional

    def deleted(self) -> int:
        return self._deleted

    def position(self) -> int:
        return self._position

    def unit(self) -> str:
        return self._unit

    def refid(self):
        return self._refid

    def amount(self) -> int:
        """ Return amount as integer if it if one"""
        if self._amount is None:
            return None
        if int(self._amount) == float(self._amount):
            return int(self._amount)
        else:
            return float(self._amount)

    def rangeamount(self):
        return self._rangeamount

    def item(self) -> str:
        return self._item


class IngredientGroup:
    def __init__(self, name: Optional[str], ingredients: Sequence[Ingredient]):
        self._name = name
        self._ingredients = sorted(ingredients, key=lambda x: x.position())
        if len(self._ingredients) > 0:
            self._id = self._ingredients[0].position()
        else:
            self._id = 0

    def name(self) -> Optional[str]:
        return self._name

    def id(self):
        """Return a high id fo that all these ingredients are listed at the button"""
        if self._name is None:
            return 10000
        return self._id

    def ingredients(self) -> Sequence[Ingredient]:
        """Return the sorted ingredients"""
        return self._ingredients


class Recipe:
    def __init__(self, id: int, title: str, instructions: str, notes: str, cuisine: str, rating: int, description: str,
                 source: str, preptime: int,
                 cooktime: int, servings: int, yields: int, yield_unit: str, image: str, thumb: str, deleted: int,
                 link: str, last_modified: float):
        self._id = id;
        self._title = title;
        self._instructions = instructions
        self._notes = notes
        self._cuisine = cuisine
        self._rating = rating
        self._preptime = preptime
        self._cooktime = cooktime
        self._yields = yields
        self._yield_unit = yield_unit
        self._last_modified = last_modified
        self._link = link
        self._description = description
        self._source = source
        self._image = image
        self._thumb = thumb
        self._deleted = deleted
        self._description = description
        self._servings = servings
        self._obj_ingredients = None
        # A set with all tags of this recipe
        self._tags = set()
        # Extract tags form notes
        self._create_tags()

    def has_unknown_cooktime(self):
        return (self._preptime + self._cooktime) <= 0

    def get_file_name(self):
        from core.validate_filename import convert_to_validate_filename
        return convert_to_validate_filename(self.title()) + ".pdf"

    def get_grouped_ingredients(self) -> Sequence[IngredientGroup]:
        all_groups = []
        groups = {}
        for ing in self._obj_ingredients:
            group: str = ing.inggroup()
            if group not in groups:
                groups[group] = []
            groups[group].append(ing)

        for group in groups:
            name: Optional[str] = group
            all_groups.append(IngredientGroup(name, groups[group]))
        return sorted(all_groups, key=lambda g: g.id())

    def symbolized_rating(self):
        symbols = []
        rating: int = self._rating
        for _ in range(0, 5):
            rating -= 2
            if rating >= 0:
                symbols.append("star")
            elif rating == -1:
                symbols.append("star_half")
            else:
                symbols.append("star_border")
        return symbols

    def _create_tags(self):
        lines = self._notes.splitlines()

        for line in lines:
            normalized_line: str = line.lower()
            if normalized_line not in all_tags:
                print("keyword does't exist: " + normalized_line + " in " + self.title())
            else:
                self._tags.add(normalized_line)

    def has_tag(self, name: str) -> bool:
        """Check if a recipe has a certain tag"""
        return name.lower() in self._tags

    def get_tags(self) -> Sequence[RecipeTag]:
        """Return all tags of a reipe"""
        keywords = []
        for tag in self._tags:
            keywords.append(all_tags[tag])
        return sorted(keywords, key=lambda x: x.render_priority(), reverse=False)

    def servings(self):
        return self._servings

    def description(self):
        return self._description

    def html_instruction(self):
        """The cooking instruction for rendering in a browser"""
        description: str = self.instructions()
        # preserve new lines
        description = re.sub('\n([^<])', r'<br/>\1', description)
        # preserve tabs
        description = description.replace("\t", "&emsp;&emsp;")
        return description

    def deleted(self) -> int:
        """Returns a boolean, which indictates if the recipe was removed"""
        return self._deleted

    def base64_image(self):
        """Base64 encoding of the image"""
        return base64.encodebytes(self.image()).decode("utf-8")

    def base64_thumb(self):
        return base64.encodebytes(self.thumb()).decode("utf-8")

    def image(self):
        """Binary representation of the image"""
        return self._image

    def thumb(self):
        return self._thumb

    def source(self) -> str:
        """e.g the recipe author"""
        return self._source

    def link(self) -> str:
        """A link to recipe or None"""
        return self._link

    def last_modified(self) -> float:
        """The last modified timestamp in unix format"""
        return self._last_modified

    def get_last_modified_date(self) -> str:
        """A human readable format of the last modified timestamp"""
        import datetime
        return datetime.datetime.utcfromtimestamp(self._last_modified).strftime('%d-%m-%Y %H:%M')

    def id(self) -> int:
        """The internal id of the recipe"""
        return self._id;

    def title(self) -> str:
        """The name of the recipe"""
        return self._title

    def instructions(self) -> str:
        """The cooking instructions"""
        return self._instructions

    def cuisine(self) -> str:
        return self._cuisine.split("/")[-1].strip()

    def get_cuisine_hierarchy(self) -> str:
        return self._cuisine

    def rating(self) -> int:
        return self._rating

    def total_time(self):
        """Preperation + Cookingtime"""
        if self.has_unknown_cooktime():
            return "N.A."

        return format_timespan(self._preptime + self._cooktime)

    def preptime(self) -> str:
        if self.has_unknown_cooktime():
            return "N.A."
        return format_timespan(self._preptime)

    def cooktime(self) -> str:
        if self.has_unknown_cooktime():
            return "N.A."
        return format_timespan(self._cooktime)

    def yields(self) -> float:
        if int(self._yields) == self._yields:
            return int(self._yields)
        return self._yields

    def yields_unit(self) -> str:
        return self._yield_unit.capitalize()
