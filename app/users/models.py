from app import db
from app.users import constants as USER

"""class Base(db.Model):
	__abstract__ = True
	id           = db.Column(db.Integer,
		primary_key=True)
	date_created = db.Column(db.DateTime,
		default=db.func.current_timestamp())
	date_modified= db.Column(db.DateTime,
		default=db.func.current_timestamp(),
		onupdate=db.func.current_timestamp())

	class Meta:
		ordering = (('date_created','desc'),)"""


class User(db.Model):

	__tablename__ = 'users'
	id 			  = db.Column(db.Integer, primary_key=True)
	username	  = db.Column(db.String(50), nullable=False, unique=True)
	email		  = db.Column(db.String(50), nullable=False, unique=True)
	password	  = db.Column(db.String(80), nullable=False)
	role		  = db.Column(db.SmallInteger, nullable=False, default=USER.USER)
	status		  = db.Column(db.SmallInteger, nullable=False, default=USER.ACTIVE)

	def __init__(self, username=None, email=None, password=None):
		self.username = username
		self.email = email
		self.password = password

	def __repr__(self):
		return '<User %r>' % (self.username)

	def getStatus(self):
		return USER.STATUS[self.status]

	def getRole(self):
		return USER.ROLE[self.role]

	def isAdmin(self):
		if self.role == USER.ADMIN:
			return True
		return False
