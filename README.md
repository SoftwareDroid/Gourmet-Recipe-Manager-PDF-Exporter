# Gourmet Recipe PDF Exporter v1

## Motivation
This program is intended to export the recipes in the *Gourmet Recipe Manager* (https://thinkle.github.io/gourmet/) as a pdf file.
The requirements are:
1. **Automation Support:** Export the recipes even if Gourmet Recipe Manager isn't running.
2. **Modern PDF design:** Beautiful PDFs
3. **Searches:** Preprocessed searches on all recipes. For example, a list of all recipes that are vegetarian.

## Usage
This program is used via commandline. An example call might be 

**Example:** main.py -db_dir /home/user/.gourmet/recipes.db -export_dir /home/user/cooking -include_images -link_dir /home/user/cooking -builder "User (builder)"

* *db_dir* the absolute path to the Gourmet Recipe Manager database
* *export_dir* where to save the exported data.
* *include_images* omit if this option if you need small pdf documents.
* *link_dir* this prefix is used in the searches to link to the recipes. This can be used for example to link to an sdcard on a smartphone.
* *builder* A string which is added as metadata to all recipes
* *disable_cache* use this option to enforce to recreate all recipes. By default only missing recipes in the export folder or updated in the database will be exported.

### Customizing
Under *example/customizing* is an example for custom recipe tags and custom recipe searches.
The notes field of the gourmet recipe manager is interpreted as list of tags.
Each line is interpreted as a tag.
e.g. Vegan\nFavorite will result, that the recipe has the tags *Vegan* and *Favorite* set.
 

## Software-Architecture
This program works after the following principle
1. Read recipe from the gourmet database
2. Create html version of the recipe with a html template engine. The templates are saved in templates folder.
3. Create pdf from html version of the recipe
4. Recreate the search documents which can link to the recipes.