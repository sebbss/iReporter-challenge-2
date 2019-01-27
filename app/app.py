from flask import Flask
from app.models.db import Database



app = Flask(__name__)
from app.routes.routes import *
from app.routes.user import *
app.config['SECRET_KEY'] = 'sebbss'
db = Database()
db.create_db_tables()

