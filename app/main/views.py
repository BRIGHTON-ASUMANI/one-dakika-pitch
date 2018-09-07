from flask import render_template,request,redirect,url_for,abort
from . import main
# from ..models import User
from .. import db
from flask_login import login_required, current_user
from .forms import *

@main.route('/', methods = ['GET','POST'])
def index():
    title = 'Welcome to One Minute Pitch'

    return render_template('index.html', title = title)

@main.route('/category/<int:id>', methods = ['GET','POST'])
def category():

    title = 'Categories'
    return render_template('category.html', title = title)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)
