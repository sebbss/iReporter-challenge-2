from flask import Flask
from app.models.db import Database



app = Flask(__name__)
from app.routes.flags import *
from app.routes.user import *
from app.routes.interventions import *
app.config['SECRET_KEY'] = 'sebbss'
db = Database()
db.create_db_tables()

