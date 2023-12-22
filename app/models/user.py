from pydantic import BaseModel, EmailStr, field_validator
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from app.main.utils import Hasher

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:test@127.0.0.1:5432/postgres'
app.config['SECRET_KEY'] = '3c4dc378e50242e3b4b5802952566fd519466210'
db = SQLAlchemy(app)
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(80), nullable=False)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)


class UserRegisterForm(BaseModel):
    username: str
    email: EmailStr
    password: str


    @field_validator('password')
    @classmethod
    def _hash_password(cls, v: str) -> str:
        return Hasher.get_password_hash(v)


class UserLoginForm(BaseModel):
    email: EmailStr
    password: str
