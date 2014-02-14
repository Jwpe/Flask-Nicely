Flask-Nicely
============

Flask-Nicely consists of a simple decorator with which to wrap Flask
functions that return data in order to turn them into pretty, consistent
JSON responses. It also provides several built in HTTP exceptions which can
be raised in a Flask function in order to return the corresponding HTTP
error response.

Documentation
-------------

Docs can be found at http://flask-nicely.readthedocs.org/

Usage
-----

The Flask-Nicely decorator is used as follows:

.. code:: python

    import flask_nicely

    app = Flask(__name__)

    @app.route('/hello/<name>')
    @flask_nicely.nice_json
    def hello(name):

        data = {
            "Name": name,
            "Message": "Hello, {}!".format(name)
        }

        return data

Wrapping our view function in the decorator will cause the view to return a
`200 OK` JSON response containing `"status": "200"`, `"error": null` and `"data"`
containing whatever is returned from the view, assuming it is able to be JSONified.

Flask-Nicely also allows you to throw HTTP exceptions which will result in a
properly formed HTTP error response. Custom exception messages may be entered:

.. code:: python

    @app.route('/error/404')
    @flask_nicely.nice_json
    def throw_404():

        raise NotFound("Could not find the grail!")

This will result in the following 404 response:

.. code:: json

    {
      "data": null,
      "error": "Could not find the grail!",
      "status": "404"
    }


An example app can be found in the examples directory, and can be run from
the root directory using:

.. code:: python

    python examples/app.py