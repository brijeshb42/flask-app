from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, PasswordField

from wtforms.validators import Required, EqualTo, Email

class LoginForm(Form):
	username = TextField('username',validators = [Required()])
	password = PasswordField('password',validators = [Required()])
	remember_me = BooleanField('remember_me', default = False)

class SignupForm(Form):
	username = TextField('Username',validators = [Required()])
	email    = TextField('Email', validators = [Required(), Email()])
	password = PasswordField('Password',validators = [Required()])
	cpassword = PasswordField('Confirm Password',validators = [
		Required(),
		EqualTo('password', message='Passwords do not match')
		])

class ForgotForm(Form):
	email    = TextField('email', validators = [Required(), Email()])
