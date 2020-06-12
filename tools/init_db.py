from app import db
from app.model.models import User
import secrets

db.create_all()

token = secrets.token_urlsafe(64)
print("Added Admin user Patrick with token:", token)

u = User(username='patrick', token=token, role="admin")
db.session.add (u)
db.session.commit()
print(User.query.all())