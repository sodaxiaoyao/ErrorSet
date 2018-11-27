import functools


# TYPE: Built-in module


def _help():
    # 交互界面查看文档，使用help(),退出quit
    pass
    # 功能：函数拓展工具包


def _cmp_to_key():
    # 生成比较内容,和排序等函数混用
    functools.cmp_to_key(lambda x, y: x - y)


def _partial():
    # 预定义参数的装饰器
    def add(a, b):
        return a + b

    add3 = functools.partial(add, 3)
    add5 = functools.partial(add, 5)
    print(add3(4))
    print(add5(10))


def _reduce():
    # 逐步计算函数
    functools.reduce(lambda x, y: x + y, range(10))


if __name__ == "__main__":
    # _help()
    pass
