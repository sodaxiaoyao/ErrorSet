import threading
from threading import Lock, RLock, Condition, Event


# TYPE: Built-in module

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
    # 功能：传统多线程


def _thread():
    # 创建线程
    return threading.Thread(name='z_1', target=test_gcd, args=(12, 13))


def _start(t: threading.Thread):
    # 开始线程
    t.start()
    t.join()  # 阻塞主进程


def _current_thread():
    # 获取当前线程
    threading.currentThread()


def _active_count():
    # 返回正在运行的线程数量
    threading.activeCount()


def _enumerate():
    # 返回一个包含正在运行的线程的list
    threading.enumerate()


def _timeout():
    # 设置全局超时时间
    threading.TIMEOUT_MAX = 10


def _set_daemon(t: threading.Thread):
    # 守护线程
    t.setDaemon(True)


def _is_alive(t: threading.Thread):
    # 线程是否在运行
    t.is_alive()


def _name(t: threading.Thread):
    # 线程名称
    t.setName('z_2')
    t.getName()


def _lock():
    # 锁
    ll = Lock()
    ll.acquire()
    ll.release()
    ll.locked()

    rl = RLock()
    rl.acquire()
    rl.release()
    # RLock允许在同一线程中被多次acquire。
    # 而Lock却不允许这种情况。
    # 注意：如果使用RLock，那么acquire和release必须成对出现，
    # 即调用了n次acquire，必须调用n次的release才能真正释放所占用的琐。


def _condition():
    # 等待池
    c = Condition()
    c.acquire()
    c.release()

    c.notify()
    c.wait()


def _event():
    # 时间
    e = Event()
    e.is_set()

    e.wait()
    e.set()
    e.clear()


def _timer():
    # 定时器
    def func():
        print('hello timer!')

    timer = threading.Timer(5, func)
    timer.start()


def _local():
    # 线程变量
    local = threading.local()
    local.name = 'main'


if __name__ == "__main__":
    # _help()
    pass
