import tornado
import tornado.gen
import tornado.escape
import tornado.options
import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.httpclient
import tornado.ioloop


# TYPE: Third-party package

def _help():
    # 交互界面查看文档，使用help(),退出quit
    pass
    # 功能：异步IO的WEB服务器框架


def hello_methods(self):
    # 自定义方法
    print(self)
    return 'hello,world'


class HelloModule(tornado.web.UIModule):
    # 自定义模块

    def __init__(self, handler):
        super(HelloModule, self).__init__(handler)

    def render(self, *args, **kwargs):
        return '<h1>Hello, UIModule!</h1>'


class RedirectHandler(tornado.web.RedirectHandler):
    # 继承处理方法
    __redirect_url = None

    def __init__(self, application, request, **kwargs):
        super(RedirectHandler, self).__init__(application, request, **kwargs)

    def initialize(self, **kwargs):
        super(RedirectHandler, self).initialize(**kwargs)
        self.__redirect_url = kwargs.get("url", "/")

    def data_received(self, chunk):
        pass

    @tornado.gen.coroutine
    def get(self):
        self.redirect(self.__redirect_url)

    @tornado.gen.coroutine
    def post(self):
        self.get()


class SocketHandler(tornado.websocket.WebSocketHandler):
    # WEB socket实现方法
    bottle = set()

    def data_received(self, chunk):
        pass

    def open(self):
        self.bottle.add(self)
        for c in self.bottle:
            c.write_message("open socket")

    def on_message(self, message):
        for c in self.bottle:
            c.write_message(message)

    def on_close(self):
        self.bottle.remove(self)

    def check_origin(self, origin):
        return True

    @classmethod
    def write_all_msg(cls, msg):
        for c in cls.bottle:
            c.write_message(msg)


class IndexHandler(tornado.web.RequestHandler):
    """
    request(uri,host,method,,header,body,path,query,version,remote_ip,files)
    """

    def __init__(self, application, request, **kwargs):
        super(IndexHandler, self).__init__(application, request, **kwargs)
        self.session_id = "tornado_session"

    @tornado.gen.coroutine
    def fetch_api(self, url, headers=None, method="GET", body=None):
        # 异步访问客户端
        resp = yield tornado.httpclient.AsyncHTTPClient().fetch(
            url,
            method=method,
            body=body,
            headers=headers,
            validate_cert=False
        )
        return resp

    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        # GET 请求方法
        # JSON数据转换
        tornado.escape.json_decode(tornado.escape.json_encode("zyp"))
        result = yield self.fetch_api("https://www.baidu.com")
        if result.code == 200:
            print(result)

    @tornado.web.authenticated
    def post(self, *args, **kwargs):
        # POST 请求方法
        self.set_header('Content-Type', 'application/octet-stream')
        self.set_header('Content-Disposition', 'attachment; filename=down_file')
        self.write("data")
        self.finish()
        self.send_error(404)

    def data_received(self, chunk):
        pass

    def initialize(self):
        # 初始化执行的方法
        pass

    def prepare(self):
        # 请求前执行的方法
        pass

    def get_current_user(self):
        # 获取安全cookie，此方法被登录验证调用
        return self.get_secure_cookie(self.session_id)

    def set_current_user(self, value):
        # expires当前时间戳加上过去的时间，设置安全cookie
        self.set_secure_cookie(self.session_id, value, expires=17200)

    def clear_current_user(self):
        # 删除安全cookie
        self.clear_cookie(self.session_id)

    def write_error(self, status_code, **kwargs):
        # 收到错误信息，执行的方法
        if status_code == 404:
            self.write("自定义：404")
        else:
            self.write('<h1 style="text-align:center">Serious (%s): The server reported a lot of errors!</h1>' % str(
                status_code))

    def set_default_headers(self):
        # 设置默认返回头内容
        self.set_content_type(0)

    def set_content_type(self, content_type=0):
        # 单独设置返回头内容
        self.set_header('Content-Type',
                        ["text/html; charset=UTF-8", "application/json; charset=UTF-8", "image/png"][content_type])

    def on_finish(self):
        # 请求结束
        print("结束了")


def _tor_log():
    # Tornado 日志设置
    tornado.options.logging = "WARNING"
    tornado.options.log_file_prefix = "./log/tor_status_{0}.log".format(80)
    tornado.options.log_rotate_mode = 'time'
    tornado.options.log_rotate_when = 'D'
    tornado.options.log_rotate_interval = 1


def _server():
    # 简单服务器生成
    tornado.options.define("port", default=80, type=int, help="Run on the given port")
    _tor_log()
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(tornado.web.Application(
        handlers=[
            (r"/", tornado.web.RequestHandler),
            (r"/login", tornado.web.StaticFileHandler),
            (r"/.*?", tornado.web.RedirectHandler, {"url": "/"}),
        ],
        **{
            'debug': True,
            'template_path': './',
            'static_path': './',
            'cookie_secret': '61oETzKXQAGaYdghdhgfhfhfg',
            'xsrf_cookies': False,
            'login_url': '/login',
            'ui_methods': {
                "hello_methods": hello_methods
            },
            'ui_modules': {
                "hello": HelloModule
            }
        }
    ),
        max_buffer_size=504857600,
        max_body_size=504857600,
        xheaders=True)
    http_server.bind(tornado.options.options.port, "127.0.0.1")
    # 值为None或者小于等于0：开启对应CPU的线程个数，其它按照值的大小开启
    http_server.start(1)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    # _help()
    pass
