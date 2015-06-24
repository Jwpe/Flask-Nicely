from functools import wraps

from .handlers import DefaultSuccessHandler, DefaultExceptionHandler
from .renderers import JSONRenderer


def nice_json(func, success_handler=DefaultSuccessHandler,
        exc_handler=DefaultExceptionHandler, renderer=JSONRenderer):

    """A decorator which returns a pretty jsonified response when wrapped
    around a Flask view function.

    :param func: the Flask view function to be wrapped
    :rtype: :class:`flask.Response`
    """

    @wraps(func)
    def json_data_or_error(*args, **kwargs):

        try:
            data = func(*args, **kwargs)
            response = success_handler(renderer_class=renderer).handle(data)

        except Exception as e:

            response = exc_handler(renderer_class=renderer).handle_exception(e)

        return response

    return json_data_or_error
