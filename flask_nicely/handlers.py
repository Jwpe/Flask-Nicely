from flask import current_app

from .errors import HTTPError, ServerError


class BaseHandler(object):

    renderer_class = None

    def __init__(self, renderer_class):

        self.renderer_class = self.renderer_class or renderer_class


class DefaultSuccessHandler(BaseHandler):

    def handle(self, data, status=200):

        response_body = {
            "data": data,
            "status": status,
            "error": None
        }

        response = self.renderer_class().render(response_body)
        response.status_code = status
        return response


class DefaultExceptionHandler(BaseHandler):

    def handle_exception(self, e):

        if isinstance(e, HTTPError):

            data = e.payload
            data.update(status=e.status_code, error=e.error_message, data=None)

            response = self.renderer_class().render(data=data)
            response.status_code = e.status_code
            return response

        else:

            if current_app.config['DEBUG'] or current_app.config['TESTING']:
                raise e
            else:
                return self.handle_exception(ServerError())
