from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.fields.html5 import  DateField
from wtforms.validators import DataRequired, EqualTo, Email


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password2',message='The passwords must match')])
    password2 = PasswordField('Re-enter password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),Email()])
    extra = SelectField('Choose one',choices=['Yes','No'])
    fecha_de_nacimeinto = DateField('Fecha de Nacimiento', format="%d/%m/%Y")
    register = SubmitField('Register')

