from flask import render_template
from . import auth
from . import auth
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from ..models import User
from .forms import LoginForm, RegistrationForm
from .. import db


@auth.route('/login', methods = ["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user, login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or password')

    title = "Login"
    return render_template('auth/login.html', title = title, login_form = login_form)





@auth.route('/register', methods = ["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.login'))
        flash('Your account was registered successfully. You can now log in.')

    title = "New Account created"
    return render_template('auth/register.html', title = title, registration_form = form)




@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
