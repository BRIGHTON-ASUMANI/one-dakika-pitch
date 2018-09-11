from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    pitch = TextAreaField('New Pitch')
    submit = SubmitField('Submit')

class TechcomForm(FlaskForm):
    comments = TextAreaField('New Pitch')
    submit = SubmitField('Submit')
