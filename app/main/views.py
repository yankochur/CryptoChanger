from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_user
from pydantic import ValidationError

from app.main.utils import get_balances
from app.models.user import UserLoginForm, UserRegisterForm, User, db


main = Blueprint("main", __name__, template_folder="templates", static_folder="static")


@main.route('/')
@main.route('/main')
def index_html():
    return render_template('/main/index.html', data=get_balances())


@main.route('/account')
def account_html():
    return render_template('/main/account.html')


@main.route('/authorization', methods=['GET', 'POST'])
def authorization_html():
    if request.form.get('email') and request.form.get('password'):
        try:
            loginform: UserLoginForm = UserLoginForm(
                email=request.form['email'],
                password=request.form['password']
            )
            # login_user(User)
        except ValidationError:
            flash("Incorrect email form")
            return redirect(url_for('main.authorization_html'))
        print(loginform)
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
            new_user = User(username=new_user.username, email=new_user.email, password=new_user.password)
            db.session.add(new_user)
            db.session.commit()
            print(new_user)
            return redirect(url_for('main.authorization_html'))
        except ValidationError:
            print('дебил неправильно заполнил регистрацию')
            return redirect(url_for('main.authorization_html'))

    return render_template('main/authorization.html')
