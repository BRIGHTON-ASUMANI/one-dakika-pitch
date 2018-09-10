from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User,Category
from .. import db,photos
from flask_login import login_required, current_user
from .forms import UpdateProfile,CategoryForm
import markdown2

@main.route('/', methods = ['GET','POST'])
def index():
    categories = Category.query.all()
    pitches = Pitch.query.all()
    categories = Category.get_categories()
    form = CategoryForm()
    if form.validate_on_submit():
        name = form.categoryname.data
        new_category = Category(categoryname = name)
        new_category.save_category()
        return redirect(url_for('main.index'))

    title = 'Welcome to One Minute Pitch'

    return render_template('index.html', title = title, category_form = form)



@main.route('/category/<int:id>', methods = ['GET','POST'])
def category(id):
    category = Category.query.get(id)

    if category is None:
        abort(404)

    title = 'Categories'
    return render_template('category.html', title = title, category = category)

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
