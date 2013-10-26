
class ErrorResponse(Exception):

    status = "500"

    def __init__(self, error_message=None, **kwargs):

        Exception.__init__(self)
        self.error_message = error_message or "Error"

class NotFound(ErrorResponse):

    status = "404"
