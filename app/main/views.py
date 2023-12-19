from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_user
from pydantic import ValidationError

from app.main.utils import get_balances
from app.models.user import UserLoginForm
from app.models.user import User


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
    data = request.form['username']
    print(data)
    return render_template('main/authorization.html')
