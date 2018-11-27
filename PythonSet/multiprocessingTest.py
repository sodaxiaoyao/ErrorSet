import multiprocessing


# TYPE: Built-in package

def test_gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            print(i)
            return i


def _help():
    # 交互界面查看文档，使用help(),退出quit
    pass
    # 功能：传统多进程


def _process():
    # 创建基本进程
    for i in range(10):
        p = multiprocessing.Process(name='name of process', target=test_gcd, args=((i, i + 8),))
        p.daemon = True
        p.start()
        print(p.is_alive())
        print(p.name)
        print(p.pid)
        p.join()
        p.terminate()


def _pool():
    # 进程池
    multiprocessing.freeze_support()  # 预防崩溃
    pool = multiprocessing.Pool(processes=2)  # 定义最大的进程数
    pool.map(test_gcd, ((1, 2), (8, 4), (1, 2), (8, 4)))  # p必须是一个可迭代变量。
    pool.close()
    pool.join()


def _queue():
    # 进程间通信

    def write(qw):
        for value in ['A', 'B', 'C']:
            print('Put %s to queue...' % value)
            qw.put(value)

    def read(qr):
        while True:
            if not qr.empty():
                value = qr.get(True)
                print('Get %s from queue.' % value)

    q = multiprocessing.Queue()
    pw = multiprocessing.Process(target=write, args=(q,))
    pr = multiprocessing.Process(target=read, args=(q,))

    pw.start()
    pr.start()


def _other():
    # 其它内容
    multiprocessing.cpu_count()  # 返回当前系统有多少个CPU。
    multiprocessing.current_process()  # 返回当前进程对应的Process对象。
    multiprocessing.freeze_support()  # 支持打包到Windows的EXE文件
    multiprocessing.active_children()  # 返回当前进程所有活动子进程列表。


if __name__ == "__main__":
    # _help()
    pass
