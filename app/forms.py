from wtforms.fields import (
    BooleanField, DateField, StringField, SubmitField, TextAreaField, TimeField
)
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


class AppointmentForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    start_date = DateField('start_date', validators=[DataRequired()])
    start_time = TimeField('start_time', validators=[DataRequired()])
    end_date = DateField('end_date', validators=[DataRequired()])
    end_time = TimeField('end_time', validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])
    private = BooleanField('private')
    submit = SubmitField('submit')
