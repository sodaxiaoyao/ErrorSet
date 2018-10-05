import itertools


# TYPE: Built-in module

def _help():
    # 交互界面查看文档，使用help(),退出quit
    print(itertools.__doc__)


def _count():
    # 生成公差为2，开始为1的等差数列
    itertools.count(1, 2)


def _cycle():
    # 循环迭代序列，遍历的时候是一直在跑的
    itertools.cycle([1, 2, 3, 4, 5])


def _repeat():
    # 循环一个元素n次
    itertools.repeat("n", 5)


def _chain():
    # 以此遍历传入序列
    itertools.chain([1, 2, 3, 4, 5], [6, 7, 8, 9, 0])


def _compress():
    # 如果列表都为真返回第一个列表中的元素
    itertools.compress([1, 2, 3, 4, 5], [True, False, True, False, False])


def _drop_while():
    # 当func返回假的时候返回
    itertools.dropwhile(lambda x: x < 5, [1, 2, 3, 4, 5, 6])


def _take_while():
    # 当func返回真的时候返回
    itertools.takewhile(lambda x: x < 5, [1, 2, 3, 4, 5, 6])


def _group_by():
    # 相同func返回值的被分为一组
    itertools.groupby([1, 2, 3, 4, 5, 6], lambda x: x > 5)


def _i_slice():
    # 返回从开始到结束步数的序列迭代
    itertools.islice([1, 2, 3, 4, 5, 6], 0, 5, 2)


def _starmap():
    # 对序列每个元素被func执行
    itertools.starmap(pow, [(1, 2), (5, 6)])


def _tee():
    # 把一个迭代器分为n个
    itertools.tee(iter([1, 2, 3, 4, 5]), 2)


def _i_zip():
    # zip 函数的迭代形式,直到耗尽停止
    itertools.zip_longest([1, 2, 3], [4, 5, 6])


def _permutations():
    # 任意取三个排列
    itertools.permutations([1, 2, 3, 4, 5], 3)


def _product():
    # 笛卡尔积
    itertools.product([1, 2, 3], [4, 5, 6])


def _combinations():
    # 迭代出所有组合
    itertools.combinations([1, 2, 3, 4, 5, 6], 2)


def _combinations_with_replacement():
    # 迭代出所有组合,包含重复的
    itertools.combinations_with_replacement([1, 2, 3, 4, 5, 6], 2)


if __name__ == "__main__":
    # _help()
    pass
