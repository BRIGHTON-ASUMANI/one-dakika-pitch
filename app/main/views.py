from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User, Comment, Pitch, Category
from .. import db,photos
from flask_login import login_required, current_user
from .forms import *
import markdown2



@main.route('/', methods = ['GET','POST'])
def index():
    categories = Category.query.all()
    pitches = Pitch.query.all()
    categories = Category.get_categories()
    title = 'Welcome to One Minute Pitch'
    form = CategoryForm()


    if form.validate_on_submit():
        name = form.name.data
        # description = form.description.data
        new_category = Category(name=name)
        new_category.save_category()
        return redirect(url_for('.index'))

    return render_template('index.html', title = title, categories = categories, pitches=pitches, cat_form=form)

@main.route('/category/<int:id>')
def category(id):

    category = Category.query.get(id)

    if category is None:
        abort(404)

    pitches = Pitch.get_pitches(id)
    title = "Pitches"
    return render_template('category.html', title = title, category = category,pitches = pitches)

@main.route('/category/pitch/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_pitch(id):
    form = PitchForm()
    category = Category.query.filter_by(id=id).first()

    if category is None:
        abort(404)

    if form.validate_on_submit():
        content = form.content.data
        # user = current_user._get_current_object()
        new_pitch = Pitch(content=content,user_id=current_user.id,category_id=category.id)
        new_pitch.save_pitch()
        return redirect(url_for('.category', id = category.id))

    title = 'New pitch'
    return render_template('pitch.html', title = title, pitch_form = form)

# Dynamic routing for one pitch
@main.route('/pitch/<int:id>', methods = ['GET','POST'])
@login_required
def single_pitch(id):

    pitches = Pitch.query.get(id)

    if pitches is None:
        abort(404)

    comment = Comment.get_comment(id)
    title = 'comment Section'
    return render_template('comment.html', title = title, pitches = pitches, comment = comment)



@main.route('/pitch/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    form = CommentForm()
    pitches = Pitch.query.filter_by(id=id).first()

    if pitches is None:
        abort(404)

    if form.validate_on_submit():
        # comment_section_id =
        new_comment = Comment(comment_section_id=form.comment.data,user_id=current_user.id,pitches_id=pitches.id)
        new_comment.save_comment()
        return redirect(url_for('.single_pitch', id = pitches.id))

    title = 'New Comment'
    return render_template('comments.html', title = title, comment_form = form)




























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
