from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Email, DataRequired

class LoginForm(FlaskForm):
	email = StringField(u'Email', validators=[DataRequired()])
	password = PasswordField(u'Password', validators=[DataRequired()])

class RegisterForm(FlaskForm):
	first_name = StringField(u'First Name')
	last_name = StringField(u'Last Name')
	email = StringField(u'Email', validators=[DataRequired(), Email()])
	password = PasswordField(u'Password', validators=[DataRequired()])