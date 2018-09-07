from . import db

#creating database for class user

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    comment = db.relationship("Comment", backref="user", lazy = "dynamic")
    def __repr__(self):
        return f'User {self.username}'


class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.name}'
