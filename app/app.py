from flask import Flask
from app.models.db import Database
from flask_cors import CORS



app = Flask(__name__)
cors = CORS(app, resources={r"/app/routes/user/*": {"origins": "*"}})
from app.routes.routes import *
from app.routes.user import *
app.config['SECRET_KEY'] = 'sebbss'
db = Database()
db.create_db_tables()

