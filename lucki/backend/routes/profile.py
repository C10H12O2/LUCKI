from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.app import db
from backend.models.user import User, UserSchema

profile_bp = Blueprint('profile', __name__)
user_schema = UserSchema()

@profile_bp.route("/<username>", methods = ["GET"])
def get_profile(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"error": "Profile not found"}), 404
    return jsonify(user_schema.dump(user)), 200

@profile_bp.route("/me", methods = ["GET"])
@jwt_required()
def get_my_profile(): 
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    return jsonify(user_schema.dump(user)), 200