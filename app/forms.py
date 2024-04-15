from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, HiddenField
from wtforms.fields.html5 import IntegerRangeField
from wtforms.fields import FieldList, FormField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class SkillsForm(FlaskForm):
    """A form for one or more skills"""
    submit = SubmitField('Find roles in digital')
    username = HiddenField()

