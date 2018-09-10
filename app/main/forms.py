from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class CategoryForm(FlaskForm):
    categoryname = StringField('name of desired category')
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('New comment')
    submit = SubmitField('Submit')


class PitchForm(FlaskForm):
    pitchtextarea = TextAreaField('New Pitch')
    submit = SubmitField('Submit')
