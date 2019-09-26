import os.path
import pickle


class Cache:
    enabled = True

    def __init__(self, path: str):
        self._path = path
        self._cache_changed = False

    def load_cache(self):
        if not os.path.exists(self._path):
            self._cache = {}
            self.write_cache()
        else:
            self._cache = pickle.load(open(self._path, 'rb'))
            self._remove_invalid_cache_entries()

    def _remove_invalid_cache_entries(self):
        for k, v in list(self._cache.items()):
            file_path: str = v[0]
            if not os.path.exists(file_path):
                del self._cache[k]

    def update_cache(self,recipe, path: str):
        """Saves only the last modified time"""
        self._cache[recipe.id()] = (path, recipe.last_modified())
        self._cache_changed = True

    def get_filepath(self,recipe)->str:
        return self._cache[recipe.id()][0]

    def need_disk_update(self,recipe) -> bool:
        # Enforce Update
        if not Cache.enabled:
            return True
        if recipe.id() in self._cache:
            # If the file is deleted we need an update
            return recipe.last_modified() != self._cache[recipe.id()][1]
        return True

    def changed(self):
        return self._cache_changed

    def write_cache(self):
        # Write cache only new if we changed it
        if self._cache_changed:
            print("Write Cache")
            pickle.dump(self._cache, open(self._path, "wb"))