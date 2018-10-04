import time


# TYPE: Built-in module

def _help():
    # 交互界面查看文档，使用help(),退出quit
    print(time.__doc__)


def _time():
    # 时间戳对象
    return time.time()


def _localtime():
    # 时间元组对象
    return time.localtime()


def _gm_time():
    # 格林自治时间
    return time.gmtime()


def _mk_time(local_time):
    # 时间元组转时间戳
    return time.mktime(local_time)


def _format_time():
    # 字符串转时间格式
    time.strptime("30 Nov 00", "%d %b %y")
    time.strftime('%Y', time.localtime())


def _c_time():
    # 生成c格式时间，as转化时间元组
    return time.asctime(), time.ctime()


if __name__ == "__main__":
    # _help()
    pass
