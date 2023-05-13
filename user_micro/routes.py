from flask import Blueprint, jsonify, request
from models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

user_blueprint = Blueprint("user_api_routes", __name__, url_prefix="/api/user")


@user_blueprint.route("/all", methods=["GET"])
def get_all_users():
    all_users = User.query.all()
    result = [user.serialize() for user in all_users]
    message = {"message": "Returning all users", "result": result}

    return jsonify(message)


@user_blueprint.route("/create", methods=["POST"])
def create_user():
    try:
        import pdb

        user = User()
        rq = request.get_json()

        user.username = rq["username"]
        user.password = generate_password_hash(rq["password"], method="sha256")
        user.is_admin = True
        db.session.add(user)
        db.session.commit()

        response = {"Message": "User created sucessfully", "result": user.serializer()}
    except Exception as e:
        print(str(e))
        response = {"message": f"Error has occured while saving a new user, ==> {e}"}

    return jsonify(response)
