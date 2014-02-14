from flask import json, make_response, current_app
from functools import wraps

from .errors import ErrorResponse

def nice_json(func):

    """A decorator which returns a pretty jsonified response when wrapped
    around a Flask view function.

    :param func: the Flask view function to be wrapped
    :rtype: :class:`flask.Response`
    :raises: :exc:`flask_nicely.errors.Unauthorized`,
        :exc:`flask_nicely.errors.Forbidden`,
        :exc:`flask_nicely.errors.NotFound`,
        :exc:`flask_nicely.errors.ServerError`,
        :exc:`flask_nicely.errors.GatewayTimeout`
    """


    @wraps(func)
    def json_data_or_error(*args, **kwargs):

        status = '200'
        error = None

        try:
            data = func(*args, **kwargs)

        except ErrorResponse as e:

            status = e.status
            error = e.error_message
            data = None

        except Exception as e:

            if current_app.config['DEBUG']:
                raise e
            else:
                status = '500'
                error = 'Internal Server Error'
                data = None

        response = make_response(
            json.jsonify(status=status, error=error, data=data))
        response.status = status
        return response

    return json_data_or_error