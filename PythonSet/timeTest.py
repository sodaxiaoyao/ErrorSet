import time


# TYPE: Built-in module

def _help():
    # 交互界面查看文档，使用help(),退出quit
    pass
    # 功能：传统时间戳工具


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


def _format():
    # 时间格式化串
    return {
        "y": "两位数的年份表示（00-99）",
        "Y": "四位数的年份表示（000-9999）",
        "m": "月份（01-12）",
        "d": "月内中的一天（0-31）",
        "H": "24小时制小时数（0-23）",
        "I": "12小时制小时数（01-12）",
        "M": "分钟数（00-59）",
        "S": "秒（00-59）",
        "a": "本地简化星期名称",
        "A": "本地完整星期名称",
        "b": "本地简化的月份名称",
        "B": "本地完整的月份名称",
        "c": "本地相应的日期表示和时间表示",
        "j": "年内的一天（001-366）",
        "p": "本地A.M.或P.M.的等价符",
        "U": "一年中的星期数（00-53）星期天为星期的开始",
        "w": "星期（0-6），星期天为星期的开始",
        "W": "一年中的星期数（00-53）星期一为星期的开始",
        "x": "本地相应的日期表示",
        "X": "本地相应的时间表示",
        "Z": "当前时区的名称",
        "%": "%号本身",
    }


if __name__ == "__main__":
    # _help()
    pass
