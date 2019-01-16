from app.routes.flags import *
from flask import Flask


app = Flask(__name__)

ireporter = '''<!DOCTYPE html>
				<html lang="en">
					<head>
						<meta charset="UTF-8">
						<title>iReporter</title>
					</head>
					<body>
						<h1>iReporter</h1>
						<a href="https://joseph-api.herokuapp.com/ireporter/api/v1/flags"></a>
					</body>
				</html>'''
app.route('/')
def home():
    return ireporter
