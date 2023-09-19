from flask import Blueprint, render_template, redirect

main = Blueprint("main", __name__, template_folder="templates")

@main.route('/')
def index_html():
    return render_template('main/index.html')

