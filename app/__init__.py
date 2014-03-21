from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
	return 'NOT found', 404

@app.route('/', methods = ['GET','POST'])
def index():
	return render_template('base.html')

from app.users.views import mod as usersModule
app.register_blueprint(usersModule)
