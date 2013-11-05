#coding:utf-8
import tornado
import tornado.ioloop
import tornado.web
import tornado.options
import tornado.httpserver
import tornado.gen

from tornado.options import define, options

# import zmq
# from zmq.eventloop import ioloop
# from zmq.eventloop.zmqstream import ZMQStream
# ioloop.install()
from wormhole.client import TornadoAsyncClient, TornadoClient, tornado_loop
tornado_loop()


define("port", default = 8999, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", Base),
            (r"/md5", MD5),
        ]
        settings = dict(
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)
        self.async_client = TornadoAsyncClient("127.0.0.1", 9527)
        self.client = TornadoClient("127.0.0.1", 9528)

class Base(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self):
        self.write("Hello")
        info = "dlljlfjsaldjfldsjfldsjoifdsijfoidjofdsojfosdajfosdjfosdojfjodsjofajoijoiijsoadfjo"
        self.application.async_client.get_md5(info)
        self.finish()

class MD5(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self):
        info = self.get_argument("info","")
        print info
        def _recv(main, err):
            self.write(main)
            self.finish()
        self.application.client.get_md5(_recv,info)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
