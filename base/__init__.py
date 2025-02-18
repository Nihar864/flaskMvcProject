import warnings
from datetime import timedelta

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

app = Flask(__name__)

app.secret_key = 'data'

app.config['SQLALCHEMY_ECHO'] = False

app.config['PERMENANT_SESSION_LIFETIME'] = timedelta(minutes=30)

app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3307/flask__db'

app.config['SQLALCHEMY_MAX_OVERFLOW'] = 0

db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.app_context().push()                       

from base.com import controller
