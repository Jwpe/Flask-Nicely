from flask import jsonify, current_app
from functools import wraps

from .errors import HTTPError, ServerError

def nice_json(func):

    """A decorator which returns a pretty jsonified response when wrapped
    around a Flask view function.

    :param func: the Flask view function to be wrapped
    :rtype: :class:`flask.Response`
    """


    @wraps(func)
    def json_data_or_error(*args, **kwargs):

        try:
            data = func(*args, **kwargs)

        except HTTPError as e:
            return e.get_response()

        except Exception as e:

            if current_app.config['DEBUG']:
                raise e
            else:
                return ServerError().get_response()

        return jsonify(status=200, error=None, data=data)

    return json_data_or_error