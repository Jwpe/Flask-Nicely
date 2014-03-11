Flask-Nicely
============

.. image:: https://travis-ci.org/Jwpe/Flask-Nicely.png?branch=develop
    :target: https://travis-ci.org/Jwpe/Flask-Nicely
.. image:: https://coveralls.io/repos/Jwpe/Flask-Nicely/badge.png?branch=develop
    :target: https://coveralls.io/r/Jwpe/Flask-Nicely?branch=develop

Flask-Nicely consists of a simple decorator with which to wrap Flask
functions that return data in order to turn them into pretty, consistent
JSON responses. It also provides several built in HTTP exceptions which can
be raised in a Flask function in order to return the corresponding HTTP
error response.

Docs can be found at http://flask-nicely.readthedocs.org/

Installation
------------

Flask-Nicely is available on `PyPI
<https://pypi.python.org/pypi/Flask-Nicely/>`_. The best way to install is
via pip, as follows:

.. code:: bash

    pip install flask-nicely

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

Wrapping our view function in the decorator will cause the view to return the
following 200 response:

.. code:: json

    {
      "data": data,
      "error": null,
      "status": 200,
    }

Flask-Nicely also allows you to throw HTTP exceptions which will result in a
properly formed HTTP error response. Custom exception messages may be entered:

.. code:: python

    from flask import Flask

    import flask_nicely
    from flask_nicely.errors import NotFound

    app = Flask(__name__)

    @app.route('/error/404')
    @flask_nicely.nice_json
    def throw_404():

        raise NotFound("Could not find the grail!")

This will result in the following 404 response:

.. code:: json

    {
      "data": null,
      "error": "Could not find the grail!",
      "status": 404
    }


An example app can be found in the examples directory, and can be run from
the root directory using:

.. code:: python

    python examples/app.py

Testing
-------

To run the tests for the project using py.test, simply run:

.. code:: bash

    python setup.py test

For multi-version testing, install and run tox:

.. code:: bash

    pip install tox
    tox
