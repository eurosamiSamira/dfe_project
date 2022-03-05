from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
# from wtforms.validators import DataRequired, Length, ValidationError

class ExerciseForm(FlaskForm):
    exercise = StringField('Exercise')
    reps = StringField('Reps')
    completed = BooleanField('Completed')
    submit = SubmitField('Send')
