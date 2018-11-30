import wsgiref
import wsgiref.simple_server
import wsgiref.handlers
import tornado.web
import tornado.wsgi


# TYPE: Third-party package

def _help():
    # 交互界面查看文档，使用help(),退出quit
    pass
    # 功能：WSGI Apache与python的中间件


class MainHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        self.write("Hello, world,A,WSGI")


def application(environ, start_response):
    # 名称很重要，Apache调用识别用
    if 'SCRIPT_NAME' in environ:
        tornado_app = tornado.wsgi.WSGIApplication([
            (r"/app", MainHandler),
        ])
        return tornado_app(environ, start_response)


def _server(app):
    # 临时服务器测试
    server = wsgiref.simple_server.make_server('127.0.0.1', 80, app)
    server.serve_forever()


if __name__ == "__main__":
    # _help()
    pass
