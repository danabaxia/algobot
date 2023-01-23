#defines the application's routes and viewsclass Config:
from flask import Blueprint, render_template, request, jsonify

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html')
