try:
    from httplib import responses  # Python 2.x
except ImportError:
    from http.client import responses  # Python 3.x


class HTTPError(Exception):

    """A generic error mixin from which the HTTP error responses inherit."""

    status_code = None

    def __init__(self, error_message='', payload=None, *args, **kwargs):

        """
        :param error_message: An optional custom error message that will be
        returned in an HTTP response. If not specified, the generic httplib
        response will be returned.
        :param payload: An optional dictionary of additional information
        to include in the JSON response.
        """

        super(HTTPError, self).__init__(*args, **kwargs)
        self.error_message = error_message or responses[self.status_code]
        self.payload = payload or {}


class Unauthorized(HTTPError):
    """A 401 Unauthorized HTTP error."""
    status_code = 401


class Forbidden(HTTPError):
    """A 403 Forbidden HTTP error."""
    status_code = 403


class NotFound(HTTPError):
    """A 404 Not Found HTTP error."""
    status_code = 404


class ServerError(HTTPError):
    """A 500 Internal Server Error HTTP error."""
    status_code = 500


class GatewayTimeout(HTTPError):
    """A 504 Gateway Timeout HTTP error."""
    status_code = 504
