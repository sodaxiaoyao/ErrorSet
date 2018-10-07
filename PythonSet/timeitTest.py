import timeit


# TYPE: Built-in module

def test_gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


def _help():
    # 交互界面查看文档，使用help(),退出quit
    print(timeit.__doc__)


def _timeit():
    # 测试程序运行速度
    return timeit.timeit('test_gcd((12,3))', 'from __main__ import test_gcd', number=10000)


def _repeat():
    # 测试程序运行速度
    return timeit.repeat('test_gcd((12,3))', 'from __main__ import test_gcd', number=100, repeat=5)


if __name__ == "__main__":
    # _help()
    pass
