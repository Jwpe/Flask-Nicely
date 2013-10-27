from flask import Flask

import flask_nicely
from flask_nicely.errors import NotFound

app = Flask(__name__)

@app.route('/hello/<name>')
@flask_nicely.nice_json
def hello(name):

    data = {
        "Name": name,
        "Message": "Hello, {}!".format(name)
    }

    return data

@app.route('/error/404')
@flask_nicely.nice_json
def throw_404():

    raise NotFound("Could not find the grail!")

@app.route('/error/exception')
@flask_nicely.nice_json
def throw_exception():

    raise Exception("I am an exception")

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000, debug=True)

