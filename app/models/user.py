from pydantic import BaseModel, EmailStr, field_validator

from app.main.utils import Hasher


class UserLogin:
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.__user['id'])


class UserLoginForm(BaseModel):
    email: EmailStr
    password: str

    @field_validator('password')
    @classmethod
    def _hash_password(cls, v: str) -> str:
        return Hasher.get_password_hash(v)