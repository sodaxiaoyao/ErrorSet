import gevent
from gevent import monkey
from gevent.event import Event, AsyncResult
from gevent.queue import Queue
from gevent.lock import BoundedSemaphore
from gevent.local import local as g_local


# TYPE: Third-party package


def test_job(x):
    print(x)


def _help():
    # 第三方的协程实现工具,优化了内置的[生成器],底层-greenlet
    # 直接下载编译后的模块包：https://www.lfd.uci.edu/~gohlke/pythonlibs/#gevent
    pass


def patch():
    # 非阻塞补丁
    monkey.patch_all()


def _getcurrent():
    # 获取当前协程
    gevent.getcurrent()


def _sleep():
    # 模拟耗时
    gevent.sleep(0)


def _spawn():
    # 创建任务
    g1 = gevent.spawn(test_job, 3)
    g2 = gevent.spawn(test_job, 4)
    g3 = gevent.spawn(test_job, 5)
    return g1, g2, g3


def _time_out():
    # 超时
    gevent.Timeout(2).start()


def _event():
    # 协程通信
    e = Event()
    ae = AsyncResult()
    e.wait()  # 唤醒
    e.set()  # 唤醒
    ae.wait()  # 唤醒
    ae.set('')  # 唤醒,可传递信息


def _queue():
    # 队列
    q = Queue()
    q.put(1)
    while not q.empty():
        q.get()


def _lock():
    # 锁
    sem = BoundedSemaphore(2)
    sem.acquire()
    sem.release()


def _local():
    # 协程共享数据
    g_local()


def _join(g1, g2, g3):
    # 开始执行
    g1.join()
    g2.join()
    g3.join()
    # gevent.joinall([g1, g2, g3])


if __name__ == "__main__":
    # _help()
    pass
