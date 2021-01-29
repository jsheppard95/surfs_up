from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/goodbye')
def goodbye_world():
    return 'Goodbye world'

@app.route('/one_more')
def one_more_string():
    return 'One more string'