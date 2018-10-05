import socket


# TYPE: Built-in module

def _help():
    # 交互界面查看文档，使用help(),退出quit
    print(socket.__doc__)


def _create_socket():
    # 创建socket
    return socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

    # socket.AF_UNIX : 只能用于单一的Unix系统进程间通信【family】
    # socket.AF_INET : 服务器间通信【family】

    # socket.SOCK_STREAM : 流式【type】
    # socket.SOCK_DGREAM : 数据报式【type】


def _opt_server(s):
    # 操作服务端socket对象
    s.bind(("127.0.0.1", "2222"))
    s.listen(5)
    s.accept()


def _opt_client(s):
    # 操作客户端socket对象
    s.connect(("127.0.0.1", "2222"))
    s.connect_ex(("127.0.0.1", "2222"))


def _opt_public(s):
    # 公用的操作函数
    s.recv(4096)
    s.send("hello,world")
    s.sendall("hello,world")

    s.recvfrom(4096)
    s.sendto("hello,world", ("127.0.0.1", "2222"))


def _get_info(s):
    # 获取远程连接的信息

    s.getpeername()
    # --返回远程连接地址
    s.getsockname()
    # --返回自己连接地址

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL)
    s.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    # --设置关键参数

    s.settimeout(60)
    s.gettimeout()
    # --从超时设置

    s.fileno()
    # --返回套接字文字描述符号

    s.setblocking(0)
    # --设置为非阻塞模式

    s.makefile()
    # --创建一个与套接字关联的文件


def _get_url():
    # 请求网站内容
    print('begin')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('www.baidu.com', 80))
    sock.send("GET / HTTP/1.1\r\n"
              "Host: www.baidu.com\r\n"
              "User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) "
              "AppleWebKit/537.36 (KHTML, like Gecko) "
              "Chrome/55.0.2883.87 Safari/537.36\r\n\r\n".encode('ascii'))
    response = b''
    chunk = sock.recv(4096)
    response += chunk
    print('end')
    return response


def _close(s):
    # 关闭socket
    s.close()


if __name__ == "__main__":
    # _help()
    pass
