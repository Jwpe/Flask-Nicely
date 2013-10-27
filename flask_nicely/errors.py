
class ErrorResponse(Exception):

    status = "500"
    error_message = "Error"

    def __init__(self, error_message=None, **kwargs):

        Exception.__init__(self)
        self.error_message = error_message or self.error_message

class Unauthorized(ErrorResponse):

    status = "401"
    error_message = "Unauthorized"


class Forbidden(ErrorResponse):

    status = "403"
    error_message = "Forbidden"


class NotFound(ErrorResponse):

    status = "404"
    error_message = "Not Found"


class ServerError(ErrorResponse):

    error_message = "Internal Server Error"


class GatewayTimeout(ErrorResponse):

    status = "504"
    error_message = "Gateway Timeout"
