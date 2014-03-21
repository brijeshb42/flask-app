from flask import Flask, render_template, flash, redirect, request
from users import Users
from users.forms import LoginForm

app = Flask(__name__)
app.config.from_object('config')

app.register_blueprint(Users, url_prefix='/u')

@app.route('/', methods = ['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		return 'OK'+form.username.data
	return render_template('base.html',form = form)