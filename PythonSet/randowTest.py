import random


# TYPE: Built-in module


def _help():
    # 交互界面查看文档，使用help(),退出quit
    print(random.__doc__)


def _random():
    # 0<=n<1.0,随机浮点数
    print(random.random())


def _uniform():
    # 指定范围的随机浮点数
    print(random.uniform(2, 3))


def _randint():
    # 指定范围的随机整数
    print(random.randint(2, 8))


def _randrange():
    # 指定范围的指定递增生成随机数
    print(random.randrange(2, 8, 2))


def _choice():
    # 从序列中随机获取
    print(random.choice([1, 2, 3, 4, 5]))


def _shuffle():
    # 重新排列序列
    print(random.shuffle([1, 2, 3, 4, 5]))


def _sample():
    # 从序列中获取指定数量的内容，并随机排列
    print(random.sample([1, 2, 3, 4, 5], 3))


def _seed():
    # 相同种子的生成随机数是相同的
    random.seed(1)


if __name__ == "__main__":
    # _help()
    pass
