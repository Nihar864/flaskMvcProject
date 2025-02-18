from enum import Enum

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3307/flask__db'
db = SQLAlchemy(app)


class UserRole(Enum):                           
    ADMIN = 'admin'
    USER = 'user'
    GUEST = 'guest'


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    role = db.Column(db.Enum(UserRole), nullable=False)  # Use db.Enum


# Example usage:
with app.app_context():
    db.create_all()  # Create the database tables

    new_user = User(username='abc', role=UserRole.ADMIN)
    db.session.add(new_user)
    db.session.commit()

    retrieved_user = User.query.filter_by(username='abc').first()
    print(retrieved_user.role)  # Output: UserRole.USER
    print(retrieved_user.role.value)  # Output: user
    print(retrieved_user.role == UserRole.USER)  # Output: True
