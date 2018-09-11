from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User, Technology, TechCom
# , Science, Religion, Sports, Employment
from .. import db,photos
from flask_login import login_required, current_user
from .forms import *
import markdown2



@main.route('/')
def index():

    return render_template('index.html')

@main.route('/technology', methods = ['GET','POST'])
@login_required
def technology():
    form = TPitchForm()
    title = 'Technology pitches'
    if form.validate_on_submit():
        pitch = form.pitch.data
        new_technology = Technology(pitch=pitch, user=current_user)
        new_technology.save_technology()
        return redirect(url_for('.index'))

    return render_template("technology.html", tpitch_form = form, title = title)


@main.route('/technology/<int:id>',  methods=['GET', 'POST'])
def techid(id):

    technologies = Technology.query.get(id)
    form = CommentTPitchForm()
    if form.validate_on_submit():
        techcom = form.techcom.data
        new_techcom = Techcom(techcom=techcom, technologies_id=id, user=current_user)
        new_techcom.save_techcom()

    techcom = Techcom.query.filter_by(technologies_id=id).all()
    return render_template('technology.html', pick=pick, techform=form, techcomments = techcom)

@main.route('/technologies')
def alltechpitches():
    title = 'all techpiches'
    pitches = Technology.query.all()
    return render_template("technology.html", title=title, pitches=pitches)














#
#
#
#
#
#
#
#
# #
# # @main.route('/technology/comment', methods = ['GET','POST'])
# # @login_required
# # def techpitch():
# #
# #
# #
# #     return render_template('technology.html')
#
#
#
#
#
#
#
# @main.route('/religion', methods = ['GET','POST'])
# @login_required
# def religion():
#     form = RPitchForm()
#     title = 'Create a pitch '
#     if form.validate_on_submit():
#         pitch = form.pitch.data
#         new_religion = Religion(pitch=pitch, user=current_user)
#         new_religion.save_religion()
#         return redirect(url_for('.index'))
#
#     return render_template("religion.html", rpitch_form = form, title = title)
#
# @main.route('/religion/comment', methods = ['GET','POST'])
# @login_required
# def relpitch():
#
#
#
#
#     return render_template('religion.html')
#
#
# @main.route('/science', methods = ['GET','POST'])
# @login_required
# def science():
#     form = SCPitchForm()
#     title = 'Create a pitch '
#     if form.validate_on_submit():
#         pitch = form.pitch.data
#         new_science = Science(pitch=pitch, user=current_user)
#         new_science.save_science()
#         return redirect(url_for('.index'))
#
#     return render_template("science.html", scpitch_form = form, title = title)
#
# @main.route('/science/comment', methods = ['GET','POST'])
# @login_required
# def scipitch():
#
#
#
#     return render_template('science.html')
#
#
#
#
# @main.route('/employment', methods = ['GET','POST'])
# @login_required
# def employment():
#     form = EPitchForm()
#     title = 'Create a pitch '
#     if form.validate_on_submit():
#         pitch = form.pitch.data
#         new_employment = Employment(pitch=pitch, user=current_user)
#         new_employment.save_employment()
#         return redirect(url_for('.index'))
#
#     return render_template("employment.html", epitch_form = form, title = title)
#
# @main.route('/employment/comment', methods = ['GET','POST'])
# @login_required
# def employpitch():
#
#
#
#
#     return render_template('employment.html')
#
#
# @main.route('/sports', methods = ['GET','POST'])
# @login_required
# def sports():
#     form = SPitchForm()
#     title = 'Create a pitch '
#     if form.validate_on_submit():
#         pitch = form.pitch.data
#         new_sports = Sports(pitch=pitch, user=current_user)
#         new_sports.save_sports()
#         return redirect(url_for('.index'))
#
#     return render_template("sports.html", spitch_form = form, title = title)
#
# @main.route('/sports/comment', methods = ['GET','POST'])
# @login_required
# def sportspitch():
#
#
#
#
#     return render_template('sports.html')
#
#
# @main.route('/user/<uname>')
# def profile(uname):
#     user = User.query.filter_by(username = uname).first()
#
#     if user is None:
#         abort(404)
#
#     return render_template("profile/profile.html", user = user)
#
#
# @main.route('/user/<uname>/update',methods = ['GET','POST'])
# @login_required
# def update_profile(uname):
#     user = User.query.filter_by(username = uname).first()
#     if user is None:
#         abort(404)
#
#     form = UpdateProfile()
#
#     if form.validate_on_submit():
#         user.bio = form.bio.data
#
#         db.session.add(user)
#         db.session.commit()
#
#         return redirect(url_for('.profile',uname=user.username))
#
#     return render_template('profile/update.html',form =form)
#
# @main.route('/user/<uname>/update/pic',methods= ['POST'])
# @login_required
# def update_pic(uname):
#     user = User.query.filter_by(username = uname).first()
#     if 'photo' in request.files:
#         filename = photos.save(request.files['photo'])
#         path = f'photos/{filename}'
#         user.profile_pic_path = path
#         db.session.commit()
#     return redirect(url_for('main.profile',uname=uname))
