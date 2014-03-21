from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, PasswordField

from wtforms.validators import Required, EqualTo

class LoginForm(Form):
	username = TextField('username',validators = [Required()])
	password = PasswordField('password',validators = [Required()])
	remember_me = BooleanField('remember_me', default = False)

class SignupForm(Form):
	username = TextField('username',validators = [Required()])
	email    = TextField('email', validators = [Required()])
	password = PasswordField('password',validators = [Required()])
	cpassword = PasswordField('cpassword',validators = [Required(), EqualTo(password)])

class ForgotForm(Form):
	email    = TextField('email', validators = [Required()])
