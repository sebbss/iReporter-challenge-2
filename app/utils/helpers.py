from functools import wraps
from flask import jsonify, request
from app.app import app
import jwt
import datetime
app.config['SECRET_KEY']= 'sebbss'

def encode_token(identity):
    return jwt.encode({'user':identity, 'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes = 300)},app.config['SECRET_KEY'])

def token_required(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = None
            if 'Authorization' in request.headers:
                token = request.headers['Authorization'].split(" ")[1]

            if not token:
                return jsonify({'message':'token is missing'}), 403
            try:
                current_user = jwt.decode(token, app.config['SECRET_KEY'])
            except:
                return jsonify({'message':'token is invalid'}), 403

            return f( current_user,*args,**kwargs)
        return decorated

