import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

def init_db(db,app):

    import secrets
    from app.model.user_object import User, Role, PermissionToRole, Permission
    from werkzeug.security import generate_password_hash, check_password_hash
    from app.model.permission_names import PermissionNames
    all_permissions = {}

    def set_permission(role : Role,name: str, value, all_permissions ):
        a: PermissionToRole = PermissionToRole(value=value)

        #if name not in all_permissions:
        #    p = Permission(name=name)
        #    all_permissions[name] = p
        #    db.session.add(p)
        a.permission = all_permissions[name]
        role.permission_association.append(a)
        db.session.add(a)

    with app.app_context():
        db.create_all()
        # Create the default roles
        roleAdmin = Role(name="Admin")
        roleModerator = Role(name="Moderator")
        roleAuthor = Role(name="Author")
        roleMember = Role(name="Member")
        roleGuest = Role(name="Guest")

        # Create Default Permissions
        all_permissions[PermissionNames.ADMIN_BAN_TOKEN] = Permission(default_value=0)
        all_permissions[PermissionNames.ADMIN_CREATE_TOKEN] = Permission(default_value=0)
        all_permissions[PermissionNames.ADMIN_DELETE_TOKEN] = Permission(default_value=0)
        for p in all_permissions:
            all_permissions[p].name = p
            db.session.add(all_permissions[p])
        # Set Permissions for all groups
        set_permission(roleAdmin, PermissionNames.ADMIN_BAN_TOKEN, 50, all_permissions)


        # Create an Admin user
        token = secrets.token_urlsafe(64)
        hashed_token = generate_password_hash(token, "sha256")
        adminUser = User(username='Admin', token=hashed_token)
        adminUser.roles.append(roleAdmin)

        # Apply changes to the database
        db.session.add(adminUser)

        db.session.add(roleAdmin)
        db.session.add(roleModerator)
        db.session.add(roleAuthor)
        db.session.add(roleMember)
        db.session.add(roleGuest)
        db.session.commit()