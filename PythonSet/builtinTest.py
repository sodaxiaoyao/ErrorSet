# TYPE: Built-in syntax


def _help():
    # Python项目命名规则
    naming_rules = {
        "项目": "Word_word",
        "包": "word_word",

        "模块": "wordWord",
        "类": "WordWord",

        "方法": "do_word",
        "函数": "do_word",

        "变量": "word_word",
        "常量": "WORD_WORD",

        "私有": "__word",
        "冲突": "_word",
        "魔法": "__word__"
    }
    naming_rules.update({"填充符": "fill"})


# =============================语法============================
def _bitwise():
    # 60 = 00111100 ,13 = 00001101 : 位运算符
    print(bin(60 & 13).replace("0b", "").zfill(8), ":与")
    print(bin(60 | 13).replace("0b", "").zfill(8), ":或")
    print(bin(60 ^ 13).replace("0b", "").zfill(8), ":异或")
    print(bin(~13).replace("0b", "").zfill(8), ":取反")
    print(bin(13 >> 2).replace("0b", "").zfill(8), ":右移")
    print(bin(13 << 2).replace("0b", "").zfill(8), ":左移")


# =============================函数============================
def _dir():
    # 获取对象所有属性
    print(dir(test_func))


def _attr():
    # 操作对象属性
    setattr(test_func, "test_attr", "test")
    if hasattr(test_func, 'test_attr'):
        print(getattr(test_func, 'test_attr'))


def _type():
    # 对象类型的操作
    print(isinstance(test_func, type(test_func)))


# =============================对象============================
def test_func(name, age=11, home='CHN', *args, **kwargs):
    inner = 'inner'


def function_help():
    # 交互界面查看文档，使用help(),退出quit
    print(function.__doc__)


def _code():
    # 获取函数对象的__code__属性
    code = test_func.__code__

    print(code.co_name)
    print(code.co_varnames)
    print(code.co_argcount)
    print(code.co_flags & 0b100)


# =============================列表============================
test_list = list()


def list_help():
    # 交互界面查看文档，使用help(),退出quit
    print(list.__doc__)


def _append():
    # list对象添加元素
    test_list.append(1)


def _extend():
    # list对象合并
    test_list.extend([1, 2, 3] + [3, 4, 5])


def _insert():
    # list对象插入元素
    test_list.insert(2, 0)


def _del():
    # list对象删除元素,切片是一种复制
    del test_list[0]
    test_list[:-1].remove(0)
    test_list.pop()


def _index():
    # 对内容在列表中索引，未索引到抛出异常
    print(test_list.index("1", 0, 1))


# =============================字典============================
test_dict = dict()


def _set_dict():
    # 设置字典内容
    test_dict.setdefault("test", "test")
    test_dict.update(test_dict)


def _get_dict():
    # 查看字典
    for i in test_dict:
        print(i)
    for i in test_dict.items():
        print(i)
    for i in test_dict.keys():
        print(i)
    for i in test_dict.values():
        print(i)


# =============================生成器============================
def test_generator():
    yield 0
    x = yield 1
    print(x)


def _get_gen():
    # 以__next__开始，send发送，并且返回下一个的值
    test_gen = test_generator()
    test_gen.__next__()
    test_gen.__next__()
    test_gen.send(2)
    pass


if __name__ == "__main__":
    _help()
    pass
