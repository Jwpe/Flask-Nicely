from flask_nicely import nice_json, ErrorResponse

from flask import current_app as app

class TestNiceJSON:

    def test_nice_json(self):

        with app.app_context():

            @nice_json
            def error_function():
                raise ErrorResponse

            response = error_function()