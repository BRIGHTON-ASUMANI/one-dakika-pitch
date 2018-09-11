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
    technologies = db.relationship('Technology', backref='user', lazy='dynamic')
    employment = db.relationship('Employment', backref='user', lazy='dynamic')
    sports = db.relationship('Sports', backref='user', lazy='dynamic')
    science = db.relationship('Science', backref='user', lazy='dynamic')
    religion = db.relationship('Religion', backref='user', lazy='dynamic')

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

class Technology(db.Model):
    __tablename__ = 'technologies'
    id = db.Column(db.Integer, primary_key=True)
    pitch = db.Column(db.String(255))
    posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_technology(self):
        db.session.add(self)
        db.session.commit()


class Employment(db.Model):
    __tablename__ = 'employment'
    id = db.Column(db.Integer, primary_key=True)
    pitch = db.Column(db.String(255))
    posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_employment(self):
        db.session.add(self)
        db.session.commit()

class Sports(db.Model):
    __tablename__ = 'sports'
    id = db.Column(db.Integer, primary_key=True)
    pitch = db.Column(db.String(255))
    posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_technology(self):
        db.session.add(self)
        db.session.commit()


class Science(db.Model):
    __tablename__ = 'science'
    id = db.Column(db.Integer, primary_key=True)
    pitch = db.Column(db.String(255))
    posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_science(self):
        db.session.add(self)
        db.session.commit()

class Religion(db.Model):
    __tablename__ = 'religion'
    id = db.Column(db.Integer, primary_key=True)
    pitch = db.Column(db.String(255))
    posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_religion(self):
        db.session.add(self)
        db.session.commit()















#
# class Techcom(db.Model):
#     __tablename__ = 'techcom'
#     id = db.Column(db.Integer, primary_key=True)
#     comment = db.Column(db.String(255))
#     technology_id = db.Column(db.Integer, db.ForeignKey("technologies.id"))
#     user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
#
#     def save_techcom(self):
#         db.session.add(self)
#         db.session.commit()
