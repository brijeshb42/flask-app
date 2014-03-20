from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello World'

if __name__ == '__main__':
	import sys
	if len(sys.argv)<2:
		app.run(port=5000,debug=True)
	else:
		app.run(port=int(sys.argv[1]),debug=True,use_debugger=True)