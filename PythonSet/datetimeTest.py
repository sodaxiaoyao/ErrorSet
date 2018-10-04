import datetime


# TYPE: Built-in module


def _help():
    # 交互界面查看文档，使用help(),退出quit
    print(datetime.__doc__)


def _date():
    # 对Date对象的基本操作
    my_date = datetime.date(2018, 10, 1)
    print(my_date.year)
    print(my_date.month)
    print(my_date.day)

    # 代替原来的内容
    print(my_date.replace(day=3))

    # 返回时间元组
    print(my_date.timetuple())

    # 返回星期
    print(my_date.weekday())

    # 自定义时间格式
    print(my_date.strftime("%H-%Y-%D"))

    # 返回统一规定的时间格式
    print(my_date.isoweekday())
    print(my_date.isocalendar())
    print(my_date.isoformat())

    # 表示的最大范围
    print(datetime.date.max)
    print(datetime.date.min)
    print(datetime.date.today())

    # 格式化时间戳
    print(datetime.date.fromtimestamp(999999))


def _time():
    # 对Time对象的基本操作
    my_time = datetime.time(22, 30, 00, 999999)
    print(my_time.hour)
    print(my_time.minute)
    print(my_time.second)
    print(my_time.microsecond)

    # 代替原来的内容
    print(my_time.replace(second=3))

    # 时区信息
    print(my_time.tzinfo)

    # 统一规定格式
    print(my_time.isoformat())

    # 自定义时间格式
    print(my_time.strftime("%H-%Y-%D"))

    # 表示的最大范围
    print(datetime.time.max)
    print(datetime.time.min)
    print(datetime.time.resolution)


def _datetime():
    # 对DateTime对象的基本操作
    my_dt = datetime.datetime(2018, 10, 1, 22, 30, 00, 999999)

    # 替换原来内容
    my_dt.replace(second=2)

    # 获取date或time对象
    my_dt.date()
    my_dt.time()

    # 获取时间元组
    my_dt.timetuple()

    # 返回C时间
    my_dt.ctime()

    # 获取时间戳
    my_dt.timestamp()

    # 今天日期
    datetime.datetime.today()

    # 现在时间
    datetime.datetime.now()
    datetime.datetime.utcnow()

    # 格式化时间戳
    print(datetime.datetime.fromtimestamp(999999))
    print(datetime.datetime.utcfromtimestamp(999999))

    # 根据date和time创建datetime
    print(datetime.datetime.combine(datetime.date.today(), datetime.time(0)))

    # 字符串和对象相互转化
    print(datetime.datetime.strptime("30 Nov 00", "%d %b %y"))
    print(datetime.datetime.strftime(my_dt, '%Y'))


def _timedelta():
    # 时间计算的类
    return datetime.timedelta(days=1)


if __name__ == "__main__":
    # _help()
    pass
