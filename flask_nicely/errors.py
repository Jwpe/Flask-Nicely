
class ErrorResponse(Exception):

    """A generic error response from which the HTTP error responses inherit."""

    status = "500"
    error_message = "Error"

    def __init__(self, error_message=None, **kwargs):

        """
        :param error_message: An optional custom error message that will be
        returned in an HTTP response.
        """

        Exception.__init__(self)
        self.error_message = error_message or self.error_message

class Unauthorized(ErrorResponse):
    """A 401 Unauthorized HTTP error."""
    status = "401"
    error_message = "Unauthorized"


class Forbidden(ErrorResponse):
    """A 403 Forbidden HTTP error."""
    status = "403"
    error_message = "Forbidden"


class NotFound(ErrorResponse):
    """A 404 Not Found HTTP error."""
    status = "404"
    error_message = "Not Found"


class ServerError(ErrorResponse):
    """A 500 Internal Server Error HTTP error."""
    error_message = "Internal Server Error"


class GatewayTimeout(ErrorResponse):
    """A 504 Gateway Timeout HTTP error."""
    status = "504"
    error_message = "Gateway Timeout"
