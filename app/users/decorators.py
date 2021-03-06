from functools import wraps

from flask import g, flash, redirect, url_for, request

def login_required(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		if g.user is None:
			flash(u'You need to be logged in to access this page.')
			return redirect(url_for('users.login', next=request.path))
		return f(*args,**kwargs)
	return decorated_function