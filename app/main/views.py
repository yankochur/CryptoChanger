from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_user
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


@main.route('/authorization', methods=['GET', 'POST'])
def authorization_html():
    if request.form.get('email') and request.form.get('password'):
        try:
            loginform: UserLoginForm = UserLoginForm(
                email=request.form['email'],
                password=request.form['password']
            )
            user = User.query.filter_by(email=loginform.email).first()
            if user is not None and Hasher.verify_password(loginform.password, user.password):
                login_user(user)
                print('authorized')
                return redirect(url_for('main.index_html'))
            else:
                raise ValueError("Incorrect email or password")
        except ValueError:
            flash("Incorrect email form", '')
            return redirect(url_for('main.authorization_html'))
    return render_template('main/authorization.html')


@main.route('/sign-up', methods=['POST'])
def registration_html():
    if request.method == 'POST':
        try:
            new_user: UserRegisterForm = UserRegisterForm(
                username=request.form['username'],
                email=request.form['email'],
                password=request.form['password']
            )
        except ValidationError:
            flash("nety @")

        validator = RegistrationValidator()
        errors = validator.validate_all(
            username=request.form['username'],
            password=request.form['password'],
            repeated_password=request.form['repeated_password'],
            email=request.form['email']
        )

        if errors:
            flash(errors)
            return redirect(url_for('main.authorization_html'))
        else:
            flash("Успешная регистрация")
            # db.session.add(new_user)
            # db.session.commit()
            return redirect(url_for('main.authorization_html'))
    else:
        raise ValueError('something with registration went wrong')
