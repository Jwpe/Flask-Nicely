from flask.views import MethodView

from .handlers import DefaultSuccessHandler, DefaultExceptionHandler
from .renderers import JSONRenderer


class APIView(MethodView):

    success_handler = DefaultSuccessHandler
    exc_handler = DefaultExceptionHandler
    renderer = JSONRenderer

    def dispatch_request(self, *args, **kwargs):

        try:
            data = super(APIView, self).dispatch_request(*args, **kwargs)

            response = self.success_handler(
                renderer_class=self.renderer).handle(data)

        except Exception as e:

            response = self.exc_handler(
                renderer_class=self.renderer).handle_exception(e)

        return response
