from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('New comment')
    submit = SubmitField('Submit')


class PitchForm(FlaskForm):
    pitchinfo = TextAreaField('New Pitch')
    submit = SubmitField('Submit')

class CategoryForm(FlaskForm):
    name = StringField('name of category')
    submit = SubmitField('Submit')
