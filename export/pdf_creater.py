from weasyprint.document import DocumentMetadata
from core.recipe import Recipe
from weasyprint import HTML
import constants
from jinja2 import Template
from typing import Optional


def create_search_result(query, options):
    assert "export_folder" in options, "Export folder is not defined"
    export_folder: str = options["export_folder"]
    # Read template file
    with open(constants.SEARCH_HTML_TEMPLATE) as file_:
        template = Template(file_.read())
    # render template with the recipe as argument
    html = template.render(query=query, results=query.get_results())
    target_file: str = export_folder + constants.PREFIX_SEARCH_RESULT_FOLDER + query.get_filename()
    doc = HTML(string=html).render()
    doc.write_pdf(target_file)

def create_recipe_pdf(recipe: Recipe, options) -> Optional[str]:
    """Returns the path to the exported pdf"""
    assert "cache" in options, "Missing cache"
    cache = options["cache"]
    ret: str = options["link_prefix"] + constants.PREFIX_RECIPE_FOLDER + recipe.get_file_name()
    if not cache.need_disk_update(recipe):
        # print("Skip recipe export already saved: ", recipe.get_file_name())
        return ret
    else:
        print("Export Recipe: ", recipe.get_file_name())
    export_images = options["export_images"]
    assert "export_folder" in options, "Export folder is not defined"
    assert "link_prefix" in options, "Link folder is not defined"
    export_folder: str = options["export_folder"]
    # Read template file
    with open(constants.RECIPE_HTML_TEMPLATE) as file_:
        template = Template(file_.read())
    # render template with the recipe as argument
    if recipe.image() is None:
        export_images = False
    html = template.render(recipe=recipe, export_images=export_images)

    # Create document Metadata
    meta = DocumentMetadata()
    meta.title = recipe.title()
    meta.generator = "Gourmet Recipe Manager Exporter\n(https://bitbucket.org/patrickmis/gourmet_recipe_exporter)"
    meta.authors = [options["builder"]]
    meta.description = "This file is automatically created with the Gourmet Recipe Manager Exporter.\nFor recipe changes, contact the Builder."
    doc = HTML(string=html).render()
    doc.metadata = meta
    target_file: str = export_folder + constants.PREFIX_RECIPE_FOLDER + recipe.get_file_name()
    doc.write_pdf(target_file)

    cache.update_cache(recipe,target_file)
    # assert not cache.need_disk_update(recipe),"Cache Logic Error"

    return ret
