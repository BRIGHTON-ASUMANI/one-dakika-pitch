from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class TPitchForm(FlaskForm):
    pitch = TextAreaField('New Pitch')
    submit = SubmitField('Submit')

class EPitchForm(FlaskForm):
    pitch = TextAreaField('New Pitch')
    submit = SubmitField('Submit')

class SCPitchForm(FlaskForm):
    pitch = TextAreaField('New Pitch')
    submit = SubmitField('Submit')

class SPitchForm(FlaskForm):
    pitch = TextAreaField('New Pitch')
    submit = SubmitField('Submit')

class RPitchForm(FlaskForm):
    pitch = TextAreaField('New Pitch')
    submit = SubmitField('Submit')
