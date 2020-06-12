from old.core.recipe import Recipe
from typing import List, Tuple, Callable, Optional
from old.export.pdf_creater import create_recipe_pdf, create_search_result
from old import constants
from old.cache import Cache
from old.core.validate_filename import convert_to_validate_filename


class SearchQuery:
    def __init__(self, name: str, determine_recipe_class: Callable[[Recipe], Optional[str]], sort_recipes_in_class):
        # Recipe -> class if None exclude recipe and "" is default class
        self._name = name
        self._include_recipe = determine_recipe_class
        self._sort_function = sort_recipes_in_class
        self._result = []

    def get_results(self) -> List[Tuple[str, List[Tuple[Recipe, str]]]]:
        return self._result

    def get_filename(self) -> str:
        return convert_to_validate_filename(self._name) + ".pdf"

    def name(self) -> str:
        return self._name

    def run(self, input: List[Tuple[Recipe, str]], options):
        """Executes the query and partitionates the result in classes """
        assert len(self._result) == 0, "Query is already executed"
        result_classes = {}
        for entry in input:
            result_class = self._include_recipe(entry[0])
            if result_class is not None:
                if result_class not in result_classes:
                    result_classes[result_class] = []

                result_classes[result_class].append(entry)

            # Sort the results
            for result_class in result_classes:
                result_classes[result_class] = sorted(result_classes[result_class], key=self._sort_function)
        # Convert the result in a sequence
        self._result = sorted(result_classes.items(), key=lambda t: t[0])

        # Write the result to a pdf
        create_search_result(self, options)


class RecipeSearch:
    def __init__(self, input_recipes: List[Recipe], queries: List[SearchQuery], options):
        self._input = input_recipes
        self._options = options
        self._recipe_to_export_file = {}
        self._queries = queries
        self._options["cache"] = Cache(options["export_folder"] + "/.cache.obj")

    def copy_db(self):
        from shutil import copyfile
        target_folder: str = self._options["export_folder"] + constants.PREFIX_EXPORT_DB_FOLDER
        print(self._options)
        assert "db_dir" in self._options, "DB Path not specified"
        db = self._options["db_dir"]
        dest = target_folder + "/recipes.db"
        print("Copy DB ", db, " to ", dest)
        copyfile(db, dest)
        print("Copy complete")

    def create_pdfs(self):
        """Create all pdfs"""
        self._options["cache"].load_cache()

        import os
        needed_folders = [self._options["export_folder"] + constants.PREFIX_RECIPE_FOLDER,
                          self._options["export_folder"] + constants.PREFIX_SEARCH_RESULT_FOLDER,
                          self._options["export_folder"] + constants.PREFIX_EXPORT_DB_FOLDER]
        for folder in needed_folders:
            if not os.path.exists(folder):
                os.makedirs(folder)
                print("Create folder: ", folder)
        query_input = []
        # Create Recipe PDFs
        for recipe in self._input:
            path: str = create_recipe_pdf(recipe, self._options)
            self._recipe_to_export_file[recipe.id()] = path
            query_input.append((recipe, path))
        self._options["cache"].write_cache()

        if self._options["cache"].changed():
            for query in self._queries:
                print("Run Search Query: ", query.name())
                query.run(query_input, self._options)
            self.copy_db()
        else:
            print("Skip creating searches  because there are no changes.")
