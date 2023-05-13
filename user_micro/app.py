from flask import Flask
from flask_migrate import Migrate
import models
from routes import user_blueprint
import os

app = Flask(__name__)

file_path = os.path.abspath(os.getcwd()) + "/database/user.db"

app.config["SECRET_KEY"] = "72AdaMylh5du3Q-q3Rvixw"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + file_path

models.init_app(app)
app.register_blueprint(user_blueprint)

migrate = Migrate(app, models.db)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
