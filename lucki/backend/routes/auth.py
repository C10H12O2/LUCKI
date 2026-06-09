from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from backend.app import db
from backend.models.user import User, UserSchema

auth_bp = Blueprint('auth', __name__)
user_schema = UserSchema()

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    #This is just gonna check if the username or email alr exists, if it does, it will return an error
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'This username already exists'}), 409
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'This email already exists'}), 409
    
    new_user = User(
        username=data['username'],
        email=data['email'],
        password_hash=generate_password_hash(data['password']),
        display_name=data.get('display_name', data["username"])   
    )
    
    db.session.add(new_user)
    db.session.commit()

    token = create_access_token(identity=str(new_user.id))
    return jsonify({"token": token, "user": user_schema.dump(new_user)}), 201

@auth_bp.route('/login', methods=['POST'])
def login(): 
    data = request.get_json()
    user = User.query.filter_by(email=data["email"]).first()
    
    if not user or not check_password_hash(user.password_hash, data["password"]):
        return jsonify({'message': 'Invalid email or password'}), 401
    
    token = create_access_token(identity=str(user.id))
    return jsonify({"token": token, "user": user_schema.dump(user)}), 200