
class ErrorResponse(Exception):

    def __init__(self, error_message=None, status="500", **kwargs):

        Exception.__init__(self)
        self.error_message = error_message or "Error"
        self.status = status
