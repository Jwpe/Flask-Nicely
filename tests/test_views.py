from flask import Flask, request
from flask.ext.testing import TestCase

from flask_nicely.views import APIView


class TestFlaskNicely(TestCase):

    def create_app(self):

        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    def test_get(self):

        data = {
            "name": "Sir Galahad of Camelot",
            "quest": "I seek the Grail",
            "favourite_colour": "Blue. No, yel...",
        }

        class GetAPIView(APIView):

            def get(self):
                return data

        self.app.add_url_rule('/', view_func=GetAPIView.as_view('get'))

        response = self.client.get('/')

        self.assertEqual(
            {'data': data, 'status': 200, 'error': None},
            response.json
        )

    def test_post(self):

        class PostAPIView(APIView):

            def post(self):
                return request.form

        self.app.add_url_rule('/', view_func=PostAPIView.as_view('post'))

        test_data = {"castle": "Camelot"}

        response = self.client.post('/', data=test_data)

        self.assertEqual(
            {'data': test_data, 'status': 200, 'error': None},
            response.json
        )
