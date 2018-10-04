import asyncio


# TYPE: Built-in package

@asyncio.coroutine
def test_cor():
    print("Hello world!")
    yield from asyncio.sleep(1)
    print("Hello again!")


def _help():
    # 内置对异步IO的支持
    pass


def _is_cor(cor):
    # 判断是否为协程函数
    print(asyncio.iscoroutinefunction(cor))


def _is_cor_obj(cor):
    # 判断是否为协程对象
    print(asyncio.iscoroutine(cor()))


def _get_event_loop():
    # 获取事件循环
    loop = asyncio.get_event_loop()
    return loop


def _run_until_complete(loop, cor):
    # 执行传入任务
    future = asyncio.ensure_future(cor())
    future.add_done_callback(print)
    # gather vs wait ，run_until_complete vs run_forever
    loop.run_until_complete(asyncio.gather(*[cor(), cor(), cor()]))


def _close_loop(loop):
    # 关闭事件循环
    loop.close()


def _get_url():
    # 请求网站
    @asyncio.coroutine
    def wget(host):
        print('wget %s...' % host)
        reader, writer = yield from asyncio.open_connection(host, 80)

        header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
        writer.write(header.encode('utf-8'))
        yield from writer.drain()

        while True:
            line = yield from reader.readline()
            if line == b'\r\n':
                break
            print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
        writer.close()

    loop = asyncio.get_event_loop()
    tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


if __name__ == "__main__":
    # _help()
    pass
