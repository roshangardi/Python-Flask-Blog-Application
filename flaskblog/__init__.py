from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Use render template for rendering the html pages.
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ATApePBVzvG8U438SDzzbtJtPkTT8Jfk'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Three slashes are tell sqlite that it is relative path
db = SQLAlchemy(app)

from flaskblog import routes