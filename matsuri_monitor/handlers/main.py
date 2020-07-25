import tornado.web

from matsuri_monitor import Supervisor, chat


class MainHandler(tornado.web.RequestHandler):

    async def get(self):
        """GET /_monitor"""
        self.send_error(404)
        # self.render('main.html')
