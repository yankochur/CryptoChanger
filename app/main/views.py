from flask import Blueprint, render_template, request, redirect
from app.main.utils import get_balances
from app.models.user import User
from app.flaskapp import db

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
    return render_template('main/authorization.html')
