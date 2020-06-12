from flask_jwt import jwt_required, current_identity
from . import admin
from app.model.user_database import auth
# file: server/app/admin/views.py
@admin.route('/protected')
#@jwt_required()
@auth.login_required
def protected():
    return 'Hello Admin'


