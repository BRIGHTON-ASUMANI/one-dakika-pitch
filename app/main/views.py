from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User, Technology
from .. import db,photos
from flask_login import login_required, current_user
from .forms import *
import markdown2



@main.route('/')
def index():

    return render_template('index.html')

@main.route('/technology', methods = ['GET','POST'])
def technology():
    form = PitchForm()
    title = 'Create a pitch '
        if technology is None:
        abort(404)

    if form.validate_on_submit():
        details = form.details.data
        new_technology = Technology(details=details)
        new_technology.save_technology()
        return redirect(url_for('.index'))

    return render_template("technology.html", pitch_form = form, title = title)

@main.route('/technology/comment', methods = ['GET','POST'])
def techpitch():

    return render_template('technology.html')

























@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
