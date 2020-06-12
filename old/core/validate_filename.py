import re
from slugify import slugify
# https://stackoverflow.com/questions/295135/turn-a-string-into-a-valid-filename

def convert_to_validate_filename(txt: str) -> str:
    regex_pattern = r'[^-a-z0-9_]+'
    return slugify(txt, separator='_', regex_pattern=regex_pattern)
