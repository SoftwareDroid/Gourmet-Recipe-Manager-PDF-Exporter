from flask_script import Manager, Server

from app import app
print(app.url_map)
app.run()
