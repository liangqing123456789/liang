from flask import Blueprint,request,jsonify
from flask_jwt_extended import JWTManager,create_access_token

min = Blueprint('min',__name__)

class User(object):
    def __init__(self,username,password):
        self.username=username
        self.password=password
users = {}
@min.route('/signup', methods=['POST'])
def signup():
    if not request.is_json:
        return jsonify("msg",'Missing JSON in request'),400
    username=request.json.get('username',None)
    password=request.json.get('password',None)
    if not username:
        return jsonify("msg",'Missing username parameter'),400
    if not password:
        return jsonify("msg",'Missing password parameter'),400
    if username in users:
        return jsonify("msg",'This username have used!'),201
    users[username] = User(username,password)
    return jsonify("msg",'signup success')

@min.route('/login',methods = ['POST'])
def login():
    if not request.is_json:
        return jsonify("msg",'Missing JSON in request'),400
    username = request.json.get('username',None)
    password = request.json.get('password',None)
    if (not username) or (not password):
        return jsonify("msg",'Missing username or password parameter'),400
    loginuser = users.get(username,None)
    if loginuser and loginuser.password == password:
        return jsonify(access_token = create_access_token(identity=username)),400
    else:
        return jsonify("msg","Username and password is not correct!"),401