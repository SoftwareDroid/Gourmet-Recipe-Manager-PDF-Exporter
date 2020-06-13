class PermissionNames:

    GROUP_NEED_CHANGE_POWER: str = "GROUP_NEED_CHANGE_POWER"
    # Checks if a login on the the server is possible
    BASIC_TRY_LOGIN : str = "BASIC_TRY_LOGIN"
    # Retrieves the API Version and the name
    BASIC_GET_SERVER_PUBLIC_INFO: str = "BASIC_GET_SERVER_INFO"

    # ========= Admin Functionalty =========
    # Creates a new token for groups with a lower or equal GROUP_NEED_CHANGE_POWER
    ADMIN_CREATE_TOKEN: str = "ADMIN_CREATE_TOKEN"
    ADMIN_DELETE_TOKEN: str = "ADMIN_DELETE_TOKEN"
    # Change the token without entering the old one
    ADMIN_EDIT_TOKEN: str = "ADMIN_EDIT_TOKEN"
    # Creates a ban on a token
    ADMIN_BAN_TOKEN: str = "ADMIN_BAN_TOKEN"
    ADMIN_VIEW_ALL_TOKENS: str = "ADMIN_VIEW_ALL_TOKENS"

    # ========= Manage the own user account =========
    # This is change password operation send oldToken and newToken to the server
    USER_CHANGE_OWN_TOKEN: str = "USER_CHANGE_OWN_TOKEN"
    # Return e.g the name, roles, memory
    USER_GET_OWN_INFO: str = "USER_GET_OWN_INFO"
    # View own permissions
    USER_VIEW_PERMISSIONS: str = "USER_VIEW_PERMISSIONS"
    USER_MEMORY_RESTRICTION: str = "USER_MEMORY_RESTRICTION"

    # ========= Recipes =========
    # This is also for listing all recipes
    RECIPE_SEARCH: str = "RECIPES_SEARCH"
    RECIPE_DELETE: str = "RECIPE_DELETE"
    RECIPE_CREATE: str = "RECIPE_CREATE"
    RECIPE_EDIT: str = "RECIPE_EDIT"

    # ========= STATISTIC =========
    STATISTIC_USE: str = "STATISTIC_USE"

    # ========= SHOPPING LIST =========
    SHOPPING_LIST_SYNC: str = "SHOPPING_LIST_SYNC"

    # ========= PDFS =========
    # Download recipes as pdfs
    PDF_CREATOR_USE: str = "PDF_CREATOR_USE"