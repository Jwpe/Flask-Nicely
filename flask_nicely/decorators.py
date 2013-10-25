from flask import json, make_response
from functools import wraps

from .errors import ErrorResponse

def nice_json(func):

    @wraps(func)
    def json_data_or_error(*args, **kwargs):

        status = '200'
        error = None

        try:
            data = func( *args, **kwargs)

        except ErrorResponse as e:

            status = e.status
            error = e.error_message
            data = None

        response = make_response(
            json.jsonify(status=status, error=error, data=data))
        response.status = status
        return response

    return json_data_or_error