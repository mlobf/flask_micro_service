from flask import Blueprint, jsonify
from models import db, User

user_blueprint = Blueprint("user_api_routes", __name__, url_prefix="/api/user")


@user_blueprint.route("/all", methods=["GET"])
def get_all_users():
    all_users = User.query.all()
    result = [user.serialize() for user in all_users]
    message = {"message": "Returning all users", "result": result}

    return jsonify(message)
