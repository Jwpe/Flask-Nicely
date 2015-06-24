from flask import jsonify


class RendererError(Exception):
    pass


class JSONRenderer(object):

    def render(self, data, *args, **kwargs):

        try:
            return jsonify(**data)
        except TypeError as e:
            raise RendererError(e)
