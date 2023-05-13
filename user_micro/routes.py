from flask import Blueprint, jsonify, request, make_response
from models import db, User
from flask_login import login_user, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

user_blueprint = Blueprint("user_api_routes", __name__, url_prefix="/api/user")


@user_blueprint.route("/all", methods=["GET"])
def get_all_users():
    all_users = User.query.all()
    result = [user.serializer() for user in all_users]
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


@user_blueprint.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    user = User.query.filter_by(username=username).first()

    if not user:
        response = {"message": "username does not exist"}
        return make_response(jsonify(response, 401))

    if check_password_hash(user.password, password):
        user.update_api_key()
        db.session.commit()
        login_user(user)
        response = {"message": "logged in ", "api_key": user.api_key}

        return make_response(jsonify(response, 200))

    response = {"message": "Access Denied"}
    return make_response(jsonify(response, 401))


@user_blueprint.route("/logout", methods=["POST"])
def logout():
    if current_user.is_authenticated:
        logout_user()
        response = {"message": "User logout"}
        return make_response(jsonify(response, 200))

    response = {"message": " No User logged in."}
    return make_response(jsonify(response, 401))


@user_blueprint.route("/<username>/exists", methods=["GET"])
def user_exists(username):
    user = User.query.filter_by(username=username).first()
    if user:
        response = {"result": True}
        return make_response(jsonify(response, 200))

    response = {"result": True}
    return make_response(jsonify(response, 404))


@user_blueprint.route("/", methods=["GET"])
def get_current_user():
    import pdb

    pdb.set_trace()
    if current_user.is_authenticated:
        response = {"result": current_user.serializer()}
        return make_response(jsonify(response, 200))
    else:
        response = {"message": "User not logged in"}
        return make_response(jsonify(response, 404))
