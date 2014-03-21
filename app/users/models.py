from app import db
from constants import *

class Base(db.Model):
	__abstract__ = True
	id           = db.Column(db.Integer,
		primary_key=True)
	date_created = db.Column(db.DateTime,
		default=db.func.current_timestamp())
	date_modified= db.Column(db.DateTime,
		default=db.func.current_timestamp(),
		onupdate=db.func.current_timestamp())


class User(Base):
	__tablename__ = 'users'
	username	  = db.Column(db.String(50), nullable=False, unique=True)
	email		  = db.Column(db.String(50), nullable=False, unique=True)
	password	  = db.Column(db.String(80), nullable=False)
	role		  = db.Column(sb.SmallInteger, nullable=False, default=ROLE_USER)
	status		  = db.Column(sb.SmallInteger, nullable=False, default=STAtUS_INVALID)
