from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_user
from pydantic impoort Val

from app.main.utils import get_balances, Hasher
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
        new_user: UserRegisterForm = UserRegisterForm(
            username=request.form['username'],
            email=request.form['email'],
            password=request.form['password']
        )
        if len(request.form['password']) < 8 or len(request.form['password']) > 32:
            flash('The password must be between 8 and 32 characters long')
            return redirect(url_for('main.authorization_html'))
        elif :
            pass
        else:
            new_user = User(username=new_user.username, email=new_user.email, password=new_user.password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('main.authorization_html'))
    else:
        raise ValueError('password < than 8')
