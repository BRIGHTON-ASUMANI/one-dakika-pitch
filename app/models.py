from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


class User(UserMixin,db.Model):
    __tablename__ = 'users'


    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email=db.Column(db.String(255),unique=True,index=True)
    password_hash=db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    technology = db.relationship('Technology', backref='user', lazy='dynamic')
    techcom = db.relationship('TechCom', backref='user', lazy='dynamic')
    employment = db.relationship('Employment', backref='user', lazy='dynamic')
    empcom = db.relationship('EmpCom', backref='user', lazy='dynamic')
    sports = db.relationship('Sports', backref='user', lazy='dynamic')
    spocom = db.relationship('SpoCom', backref='user', lazy='dynamic')
    science = db.relationship('Science', backref='user', lazy='dynamic')
    scicom = db.relationship('SciCom', backref='user', lazy='dynamic')
    religion = db.relationship('Religion', backref='user', lazy='dynamic')
    relcom = db.relationship('RelCom', backref='user', lazy='dynamic')

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


    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


class Technology(db.Model):
    __tablename__ = 'technology'
    id = db.Column(db.Integer, primary_key=True)
    pitch = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    tech = db.relationship('TechCom', backref='use', lazy='dynamic')

    def save_technology(self):
        db.session.add(self)

class TechCom(db.Model):
    __tablename__ = 'techcom'
    id = db.Column(db.Integer, primary_key=True)
    techcom = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    tech_id = db.Column(db.Integer, db.ForeignKey("technology.id"))

    def save_techcom(self):
        db.session.add(self)
        db.session.commit()




class Employment(db.Model):
    __tablename__ = 'employment'
    id = db.Column(db.Integer, primary_key=True)
    pitch = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    employ = db.relationship('EmpCom', backref='use', lazy='dynamic')

    def save_employment(self):
        db.session.add(self)

class EmpCom(db.Model):
    __tablename__ = 'empcom'
    id = db.Column(db.Integer, primary_key=True)
    empcom = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    employ_id = db.Column(db.Integer, db.ForeignKey("employment.id"))

    def save_empcom(self):
        db.session.add(self)
        db.session.commit()


class Sports(db.Model):
    __tablename__ = 'sports'
    id = db.Column(db.Integer, primary_key=True)
    pitch = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    sport = db.relationship('SpoCom', backref='use', lazy='dynamic')

    def save_sports(self):
        db.session.add(self)

class SpoCom(db.Model):
    __tablename__ = 'spocom'
    id = db.Column(db.Integer, primary_key=True)
    spocom = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    sport_id = db.Column(db.Integer, db.ForeignKey("sports.id"))

    def save_spocom(self):
        db.session.add(self)
        db.session.commit()



class Science(db.Model):
    __tablename__ = 'science'
    id = db.Column(db.Integer, primary_key=True)
    pitch = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    scien = db.relationship('SciCom', backref='use', lazy='dynamic')

    def save_science(self):
        db.session.add(self)

class SciCom(db.Model):
    __tablename__ = 'scicom'
    id = db.Column(db.Integer, primary_key=True)
    scicom = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    scien_id = db.Column(db.Integer, db.ForeignKey("science.id"))

    def save_scicom(self):
        db.session.add(self)
        db.session.commit()



class Religion(db.Model):
    __tablename__ = 'religion'
    id = db.Column(db.Integer, primary_key=True)
    pitch = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    relig = db.relationship('RelCom', backref='use', lazy='dynamic')

    def save_religion(self):
        db.session.add(self)

class RelCom(db.Model):
    __tablename__ = 'relcom'
    id = db.Column(db.Integer, primary_key=True)
    relcom = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    relig_id = db.Column(db.Integer, db.ForeignKey("religion.id"))

    def save_relcom(self):
        db.session.add(self)
        db.session.commit()
