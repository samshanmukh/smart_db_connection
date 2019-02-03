""" Code to display the data fetched from database"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	return "showing data from database"

@app.route('/get_data')
def data():
	import get_data as data
	return str([i for i in data.rows])

@app.route('/set_data')
def in_data():
	return None

@app.route('/delete_data')
def delete_data():
	return None

app.run(host='0.0.0.0', port=81, debug=True, load_dotenv=None)
# export FLASK_APP=`pwd`/show_data.py
# export FLASK_DEBUG=1
# flask run
# python3.5 -m flask run
