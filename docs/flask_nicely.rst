flask_nicely package
====================

Flask-Nicely consists of a simple decorator with which to wrap Flask
functions that return data in order to turn them into pretty, consistent
JSON responses. It also provides several built in HTTP exceptions which can
be raised in a Flask function in order to return the corresponding HTTP
error.

:mod:`decorator` Module
----------------------

The :mod:`decorator` module is the core function of the package.

.. automodule:: flask_nicely.decorators
    :members:
    :undoc-members:
    :show-inheritance:

:mod:`errors` Module
----------------------

The :mod:`errors` module contains a collection of exceptions that will
generate corresponding Flask HTTP responses when raised in a function.

.. automodule:: flask_nicely.errors
    :members:
    :undoc-members:
    :show-inheritance:
