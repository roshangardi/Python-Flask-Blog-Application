from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Use render template for rendering the html pages.
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ATApePBVzvG8U438SDzzbtJtPkTT8Jfk'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Three slashes are tell sqlite that it is relative path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes