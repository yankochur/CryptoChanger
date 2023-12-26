from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_user, logout_user
from pydantic import ValidationError

from app.main.validators import RegistrationValidator
from app.main.utils import get_balances, Hasher
from app.models.user import UserLoginForm, UserRegisterForm, User, db

main = Blueprint("main", __name__, template_folder="templates", static_folder="static")


@main.route('/')
@main.route('/main')
def index_html():
    return render_template('main/index.html', data=get_balances())


@main.route('/account')
def account_html():
    return render_template('main/account.html')


@main.route('/p2p')
def p2p_html():
    return render_template('main/account.html')


@main.route('/login', methods=['GET', 'POST'])
def login_html():
    if request.method == 'POST':
        try:
            loginform: UserLoginForm = UserLoginForm(
                email=request.form['email'],
                password=request.form['password']
            )
            user = User.query.filter_by(email=loginform.email).first()
            if user is not None and Hasher.verify_password(loginform.password, user.password):
                login_user(user)
                print(loginform.email, 'authorized')
                return redirect(url_for('main.index_html'))
            else:
                raise ValueError("Incorrect email or password")
        except ValueError:
            flash("Incorrect email form", category='flash-error')
            return redirect(url_for('main.login_html'))
    return render_template('main/login.html')


@main.route('/registration', methods=['GET', 'POST'])
def registration_html():
    if request.method == 'POST':
        try:
            new_user: UserRegisterForm = UserRegisterForm(
                username=request.form['username'],
                email=request.form['email'],
                password=request.form['password']
            )
        except ValidationError:
            flash("The email was entered incorrectly", category='flash-error')
            return redirect(url_for('main.registration_html'))

        registration_validator = RegistrationValidator()
        errors = registration_validator.validate_all(
            username=request.form['username'],
            password=request.form['password'],
            repeated_password=request.form['repeated_password'],
            email=request.form['email']
        )

        if errors:
            flash(errors, category='flash-error')
            return redirect(url_for('main.registration_html'))
        else:
            flash("Successful registration", "flash-success")
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('main.registration_html'))
    return render_template('main/registration.html')


@main.route('/logout', methods=['POST'])
def logout_func():
    logout_user()
    flash("Successfully logged out", "flash-simple")
    return redirect(url_for('main.login_html'))
