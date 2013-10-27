from flask import Flask
from flask.ext.testing import TestCase

from flask_nicely import nice_json, ErrorResponse

class TestFlaskNicely(TestCase):

    def create_app(self):

        app = Flask(__name__)
        app.config['TESTING'] = True
        return app


    def test_success(self):
        """
        Test that if the decorated function does not throw an exception,
        a correctly-formed JSON response is returned containing data returned
        by the function.
        """

        data = {
            "name": "Arthur, King of the Britons",
            "quest": "To seek the Holy Grail",
            "air-speed velocity of unladen swallow": "An African or a European swallow?",
            }

        @nice_json
        def success_function():
            return data

        response = success_function()

        self.assertEqual(
            {"data": data, "status": "200", "error": None},
            response.json)

        self.assertEqual(200, response.status_code)

    def test_500(self):
        """
        Test that if the decorated function throws a generic ErrorResponse
        error, a JSON response of status 500 is returned with a generic error
        message.
        """

        @nice_json
        def error_function():
            raise ErrorResponse

        response = error_function()

        self.assertEqual(
            {"data": None, "status": "500", "error": "Error"},
            response.json)

        self.assertEqual(500, response.status_code)

    def test_exception_debug(self):
        """
        Test that if the decorated function throws an unspecified exception,
        then the decorator will raise it if the app is in debug mode.
        """
        self.app.config['DEBUG'] = True

        @nice_json
        def error_function():
            raise Exception("I am an exception")

        with self.assertRaises(Exception):
            response = error_function()

    def test_exception_live(self):
        """
        Test that if the decorated function throws an unspecified exception,
        then the decorator will return a JSON response of status 500 if the app
        is not in debug mode.
        """
        self.app.config['DEBUG'] = False

        @nice_json
        def error_function():
            raise Exception("I am an exception")

        response = error_function()

        self.assertEqual(
            {"data": None, "status": "500", "error": "Internal Server Error"},
            response.json)

        self.assertEqual(500, response.status_code)
