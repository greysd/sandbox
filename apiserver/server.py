# encoding: utf-8

# Usage:
# python -m apiserver.server --port=1234 ...

from __future__ import absolute_import

import logging
import signal

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

from apiserver.route import route
from apiserver.settings import DEBUG, SERVER_PORT, PRIVATE_FILES_PATH, TEMPLATES_PATH

import apiserver.files  # noqa


class Application(tornado.web.Application):
    def __init__(self):
        handlers = route.handlers()
        handlers += [
            (r'/dl/(.*)', tornado.web.StaticFileHandler, {'path': PRIVATE_FILES_PATH}),
        ]

        settings = dict(
            debug=DEBUG,
            static_handler_class=tornado.web.StaticFileHandler,
            template_path=TEMPLATES_PATH,
        )
        tornado.web.Application.__init__(self, handlers, **settings)


def install_signal_handlers(server, graceful_shutdown_function):
    def ioloop_stop():
        tornado.ioloop.IOLoop.instance().stop()
        exit(0)

    def request_force_stop(signum, frame):
        logging.warning('Forced stop requested.')
        ioloop_stop()

    def request_stop(signum, frame):
        logging.warning('Graceful stop requested.')
        server.stop()

        signal.signal(signal.SIGINT, request_force_stop)
        signal.signal(signal.SIGTERM, request_force_stop)

        graceful_shutdown_function()
        ioloop_stop()

    signal.signal(signal.SIGINT, request_stop)
    signal.signal(signal.SIGTERM, request_stop)


def shutdown_sequence():
    pass


def main():
    define('port', help='bind server on the given port', type=int, default=SERVER_PORT)
    tornado.options.parse_command_line()

    app = Application()

    http_server = tornado.httpserver.HTTPServer(app, xheaders=True)
    install_signal_handlers(http_server, shutdown_sequence)

    http_server.listen(options.port)
    logging.debug('Listening on port %d' % SERVER_PORT)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
