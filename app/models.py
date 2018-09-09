from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__ = 'users'


    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email=db.Column(db.String(255),unique=True,index=True)
    password_hash=db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    # categories = db.relationship('Category',backref = 'user',lazy = "dynamic")


    @property
    def password(self):
        raise AttributeError('You can not read the password Attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        return  {self.username}

class Category(db.Model):

    __tablename__ = 'categories'

    id = db.Column(db.Integer,primary_key = True)
    categoryname = db.Column(db.Integer)
    # information = db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def save_category(self):

        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_categories(cls):
        categories = Category.query.all()
        return categories


class Pitch(db.Model):
    all_pitches = []
    __tablename__ = 'pitches'
    id = db.Column(db.Integer,primary_key = True)
    TextAreaField = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    category_id = db.Column(db.Integer,db.ForeignKey("categories.id"))
    comment = db.relationship("Comment", backref="pitch", lazy = "dynamic")
    upvote = db.Column(db.String(255))
    downvote = db.Column(db.String(255))


    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_pitches(cls):
        Pitch.all_pitches.clear()


    @classmethod
    def get_pitches(cls,id):
        pitches = Pitch.query.filter_by(category_id=id).all()
        return pitches




class Comment(db.Model):

    __tablename__ = 'comment'

    id = db.Column(db. Integer,primary_key = True)
    comment = db.Column(db.String(255))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    pitches_id = db.Column(db.Integer,db.ForeignKey("pitches.id"))
    upvote = db.Column(db.String(255))
    downvote = db.Column(db.String(255))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comment(self,id):
        comment = Comment.query.filter_by(pitches_id=id).all()
        return comment
