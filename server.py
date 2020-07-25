from pathlib import Path

import tornado
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import asyncio

from matsuri_monitor import Supervisor, handlers

tornado.options.define('port', default=8080, type=int, help='Run on the given port')
tornado.options.define('debug', default=False, type=bool, help='Run in debug mode')
tornado.options.define('interval', default=300, type=float, help='Seconds between updates')


def main():
    """Create app and start server"""
    supervisor = Supervisor(tornado.options.options.interval)

    # print(static_path)

    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    # required for python 3.8 to work with asyncio.

    server = tornado.httpserver.HTTPServer(
        tornado.web.Application(
            [
                (r'/_monitor', handlers.MainHandler),
            ],
            debug=tornado.options.options.debug,
        )
    )

    if tornado.options.options.debug:
        server.listen(tornado.options.options.port)
    else:
        server.bind(tornado.options.options.port)
        server.start(1)

    current_ioloop = tornado.ioloop.IOLoop.current()

    supervisor.start(current_ioloop)

    current_ioloop.start()


if __name__ == '__main__':
    tornado.options.parse_command_line()
    main()
