from flask import Flask
from flask.ext.testing import TestCase

from flask_nicely import nice_json
from flask_nicely.errors import NotFound

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
            {'data': data, 'status': 200, 'error': None},
            response.json)

        self.assertEqual(200, response.status_code)

    def test_404(self):
        """
        Test that if the decorated function throws a NotFound error, a JSON
        response of status 404 is returned with a generic error message.
        """

        @nice_json
        def error_function():
            raise NotFound()

        response = error_function()

        self.assertEqual(
            {'data': None, 'status': 404, 'error': "Not Found"},
            response.json)

        self.assertEqual(404, response.status_code)

    def test_404_custom_message(self):
        """
        Test that if the decorated function throws a NotFound error with a
        specified message, a JSON response of status 404 is returned with
        'error' set to the custom message.
        """

        @nice_json
        def error_function():
            raise NotFound("Could not find the Grail!")

        response = error_function()

        self.assertEqual(
            {'data': None, 'status': 404, 'error': "Could not find the Grail!"},
            response.json)

        self.assertEqual(404, response.status_code)

    def test_404_custom_payload(self):
        """
        Test that if the decorated function throws a NotFound error with an
        additional payload, a JSON response of status 404 is returned with
        extra keys from the payload included.
        """

        test_payload = {
            'error_detail': "The resource that you requested was not found on the server",
            'documentation': "http://www.flask-nicely.readthedocs.org",
        }

        @nice_json
        def error_function():
            raise NotFound(payload=test_payload)

        response = error_function()

        self.assertEqual({
            'data': None, 'status': 404, 'error': "Not Found",
            'error_detail': "The resource that you requested was not found on the server",
            'documentation': "http://www.flask-nicely.readthedocs.org",
            },
            response.json)

        self.assertEqual(404, response.status_code)



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
            {'data': None, 'status': 500, 'error': "Internal Server Error"},
            response.json)

        self.assertEqual(500, response.status_code)
