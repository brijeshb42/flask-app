from flask import Blueprint, render_template, request, flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash
from app import db

from app.users.forms import SignupForm, LoginForm
from app.users.models import User
from app.users.decorators import login_required

mod = Blueprint('users',__name__, url_prefix = '/u')

@mod.before_request
def before_request():
	g.user = None
	if 'user_id' in session:
		g.user = User.query.get(session['user_id'])

@mod.route('/me/')
@login_required
def home():
	return render_template('users/index.html')

@mod.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm(request.form)
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user and check_password_hash(user.password, form.password.data):
			session['user_id'] = user.id
			flash('Welcome %s' % user.username)
			return redirect(url_for('index'))
		flash('Invalid credentials.')
	return render_template('users/login.html', form=form)

@mod.route('/signup', methods=['GET','POST'])
def signup():
	form = SignupForm(request.form)
	if form.validate_on_submit():
		user = User(username=form.username.data,
			email = form.email.data,
			password = generate_password_hash(form.password.data)
			)
		db.session.add(user)
		db.session.commit()
		flash('You have been registered.')
		return redirect(url_for('index'))
	return render_template('users/signup.html', form=form)

@mod.route('/forgot', methods=['GET', 'POST'])
def forgot():
	return 'forgot'