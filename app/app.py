from flask import Flask
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)


app = Flask(__name__)
from app.routes.flags import *
from app.routes.user import *
app.config['JWT_SECRET_KEY'] = 'sebbss'
jwt = JWTManager(app)