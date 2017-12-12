# encoding: utf-8
import tornado.web

from bisect import bisect


class route(object):
    """
    Decorates RequestHandlers and builds up a list of routables handlers.

    Here is a simple "Hello, world" example app::

        import tornado.ioloop
        import tornado.web

        from route import route

        @route('/')
        class HomepageHandler(tornado.web.RequestHandler):
            def get(self):
                self.write('<a href="/say/hello">Click here</a>')

        @route('/say/hello')
        class HelloHandler(tornado.web.RequestHandler):
            def get(self):
                self.write('Hello, world!')

        if __name__ == '__main__':
            application = tornado.web.Application(route.handlers())
            application.listen(8888)
            tornado.ioloop.IOLoop.instance().start()
    """
    _routes = []
    _meta = []

    def __init__(self, url, name=None, title=None, position=None):
        self.url = url
        self.name = name
        self.position = position
        self.title = title
        if title is None and name is not None:
            self.title = name.capitalize()

    def __call__(self, handler):
        """Get called when we decorate a class."""
        name = self.name and self.name or handler.__name__
        self._routes.append(tornado.web.url(self.url, handler, name=name))

        # keep params always sorted
        keys = [x['position'] for x in self._meta]

        if keys and self.position is None:
            self.position = max(keys) + 1
        else:
            self.position = 1

        return handler

    @classmethod
    def handlers(self):
        return self._routes

    @classmethod
    def meta(self):
        return self._meta


def route_redirect(from_url, to_url, name=None):
    route._routes.append(tornado.web.url(from_url, tornado.web.RedirectHandler, {'url': to_url}, name=name))
