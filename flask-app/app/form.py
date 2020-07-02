from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class DataForm(FlaskForm):
    student_id = StringField('Student Id', validators=[Length(min=10, max=10, message='Student id not valid' ),DataRequired()])
    first_name = StringField('Student first name', validators=[DataRequired()])
    last_name = StringField('Student last name', validators=[DataRequired()])
    group=StringField('Student group', validators=[DataRequired()])
    student_email = StringField('Student email', validators=[DataRequired()])
    submit = SubmitField('Submit')


class UpdateForm(FlaskForm):
    student_id = StringField('Student Id', validators=[Length(min=10, max=10, message='Student id not valid')])
    first_name = StringField('Student first name')
    last_name = StringField('Student last name')
    group=StringField('Student group')
    student_email = StringField('Student email')
    submit = SubmitField('Update')


class SearchForm(FlaskForm):
    student_id = StringField('Student Id',validators=[Length(min=10, max=10, message='Student id not valid' ),DataRequired()])
    submit = SubmitField('Search')