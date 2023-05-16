from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
import os

file_path = os.path.abspath(os.getcwd()) + "/database/user.db"

app = Flask(__name__, static_folder='static')
app.config["SECRET_KEY"] = "72AdaMylh5du3Q-q3Rvixw"
app.config['WTF_CSRF_SECRET_KEY'] = "72AdaMylh5du3Q-q3Rvixw"
app.config['UPLOAD_FOLDER'] = "static/images"


login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_message = "Please Login"
login_manager.login_view = 'frontend.login'


bootstrap = Bootstrap(app)


@login_manager.user_loader
def load_user(user_id):
    return None





if __name__ == "__main__":
    app.run(debug=True, port=5005)
