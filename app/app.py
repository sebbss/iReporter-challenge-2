from flask import Flask


app = Flask(__name__)
from app.routes.flags import *
from app.routes.user import *