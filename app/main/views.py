from flask import Blueprint, render_template
from app.main.utils import get_balances


main = Blueprint("main", __name__, template_folder="templates")


@main.route('/')
@main.route('/main')
def index_html():
    return render_template('/main/index.html', data=get_balances())


@main.route('/account')
def account_html():
    return render_template('/main/account.html')
