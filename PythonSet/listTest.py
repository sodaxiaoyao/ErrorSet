# TYPE: Built-in object

test_obj = list()


def _help():
    # 交互界面查看文档，使用help(),退出quit
    print(list.__doc__)


def _append():
    # list对象添加元素
    test_obj.append(1)


def _extend():
    # list对象合并
    test_obj.extend([1, 2, 3] + [3, 4, 5])


def _insert():
    # list对象插入元素
    test_obj.insert(2, 0)


def _del():
    # list对象删除元素,切片是一种复制
    del test_obj[0]
    test_obj[:-1].remove(0)
    test_obj.pop()


if __name__ == "__main__":
    _help()
