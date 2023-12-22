from app.models.user import User


class RegistrationValidator:
    @staticmethod
    def validate_password(password, repeated_password):
        if (len(password) < 8
                or len(password) > 32
                or not any(char.isdigit() for char in password)
                or not any(char.isupper() for char in password)
                or not any(char.islower() for char in password)):
            return 'The password must contain Lowercase, Uppercase, The Number and must be between 8 and 32 characters long'
        elif password != repeated_password:
            return 'The password has not been confirmed'
        else:
            return None

    @staticmethod
    def validate_username(username):
        if len(username) < 3 or len(username) > 32:
            return 'The username must be between 3 and 32 characters long'
        else:
            return None

    @staticmethod
    def validate_email_unique(email):
        if User.query.filter_by(email=email).first() is not None:
            return 'That email is already used'
        else:
            return None

    @classmethod
    def validate_all(cls, password, repeated_password, username, email):
        errors = (
            cls.validate_username(username),
            cls.validate_password(password, repeated_password),
            cls.validate_email_unique(email)
        )

        error_messages = [error for error in errors if error is not None]

        return error_messages[0] if error_messages else None
