import greenlet


# TYPE: Third-party module

def test_job_1():
    print(1)
    g2.switch()
    print(2)
    g2.switch()


def test_job_2():
    print(3)
    g1.switch()
    print(4)


def _help():
    # 交互界面查看文档，使用help(),退出quit
    # 第三方的协程实现工具
    # 直接下载编译后的模块包：https://www.lfd.uci.edu/~gohlke/pythonlibs/#gevent
    pass
    # 功能：初级非自动协程支持工具


def _create_greenlet():
    # 创建greenlet对象
    return greenlet.greenlet(test_job_1), greenlet.greenlet(test_job_2)


g1, g2 = _create_greenlet()


def _switch():
    # 任务切换,可以在switch传入任务参数
    g1.switch()


def _dead():
    # 判断是否执行完毕
    g1.dead()


def _throw():
    # 切换到指定协程，并立即抛出异常
    g1.throw()


def _check():
    # 任务监控
    greenlet.settrace(lambda: 2)
    greenlet.gettrace()


if __name__ == "__main__":
    # _help()
    pass
