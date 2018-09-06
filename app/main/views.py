from flask import render_template,redirect,url_for,abort
from . import main
# from ..models import User
from .. import db
from flask_login import login_required, current_user
from .forms import *

@main.route('/', methods = ['GET','POST'])
def index():
    title = 'Welcome to One Minute Pitch'

    return render_template('index.html', title = title)
