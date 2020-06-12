import os
import sys

dirContents = os.listdir("customizing")
if not os.path.exists('customizing/custom_recipe_tags.py') or not os.path.exists(
        'customizing/custom_recipe_searches.py'):
    print(
        "The customization folder does not contain the expected files.\nSee README.md or example/customizing to set setup a valid configuration.")
    sys.exit(1)
