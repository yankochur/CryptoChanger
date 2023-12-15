from flask import Blueprint, render_template, request, redirect, flash, url_for
from pydantic import ValidationError

from app.main.utils import get_balances
from app.models.user import UserLoginForm

import flask_login


main = Blueprint("main", __name__, template_folder="templates")


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
