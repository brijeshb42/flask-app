import bottle
from bottle import request, abort
from peewee import *
import datetime
from beaker.middleware import SessionMiddleware

session_opts = {
    'session.type': 'file',
    'session.cookie_expires': True,
    'session.data_dir': './session/',
    'session.auto': True
}

app = SessionMiddleware(bottle.app(), session_opts)

"""magnet:?xt=urn:tree:tiger:OSX7DIYI7U5RHONCHRQVKR67KP6GFXOVXO3JBLI&xl=20174&dn=absentia-2011_english-664394.zip
"""

db = SqliteDatabase('test.db')

class BaseModel(Model):
	class Meta:
		database = db

class Links(BaseModel):
	id = PrimaryKeyField(null = False)
	tth = CharField(null = False, default='none', max_length=40)
	name  = CharField(null = False)
	created = DateTimeField(default=datetime.datetime.now)
	is_published = BooleanField(default=True)

beaker_session = {}

OPERATIONS = ['+','-']

@bottle.hook('before_request')
def setup_session():
	try:
		beaker_session = request.environ.get('beaker.session')
		print(beaker_session)
	except:
		abort(401,'Failed session')
	#request.session = request.environ.get('beaker.session')

@bottle.route('/')
def index():
	if 'track' in beaker_session:
		return 'OK'
	#beaker_session['track'] = 1
	beaker_session.invalidate()

if __name__ == '__main__':
	bottle.run(host='0.0.0.0',port=5000, debug=True, reloader=True)