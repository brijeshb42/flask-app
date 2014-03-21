from flask import Blueprint, render_template, request
from jinja2 import TemplateNotFound
import models

Users = Blueprint('Users',__name__)

@Users.route('/')
def index():
	return 'User account'

@Users.route('/login', methods=['GET','POST'])
def login():
	return 'login'

@Users.route('/signup', methods=['GET','POST'])
def signup():
	return 'signup'

@Users.route('/forgot', methods=['GET', 'POST'])
def forgot():
	return 'forgot'