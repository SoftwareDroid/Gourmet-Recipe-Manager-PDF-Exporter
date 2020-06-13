from flask_script import Manager, Server

from app import app

import os
#print( app.url_map)
path = os.path.abspath(os.path.dirname(__file__))
app.run(ssl_context=(path + '/cert.pem', path + '/key.pem'))
