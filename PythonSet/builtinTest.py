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


def _color():
    # 颜色控制
    display = {"默认": 0, "高亮": 1, "下划线": 4, "闪烁": 5, "反白": 7, "不可见": 8}
    foreground = [30, 31, 32, 33, 34, 35, 36, 37]
    background = [40, 41, 42, 43, 44, 45, 46, 47]
    print("\033[{};{};{}m".format(display["高亮"], foreground[2], background[3]))
    print("测试内容")
    print("\033[0m")


def test_decorator():
    # 装饰器
    def wrapper(func):
        def check(*args):
            return func(*args) + 12

        return check

    @wrapper
    def test(x):
        return x + 1

    print(test(1))


# =============================函数============================
def _dir():
    # 获取对象所有属性
    print(dir(test_func))


def _attr():
    # 操作对象属性
    setattr(test_func, "test_attr", "test")
    if hasattr(test_func, 'test_attr'):
        print(getattr(test_func, 'test_attr'))
    delattr(test_func, "test_attr")


def _type():
    # 对象类型的操作
    print(isinstance(test_func, type(test_func)))


def _enumerate():
    # 生成枚举格式
    for i, e in enumerate([1, 2, 3]):
        print(i, e)


def _id():
    # 获取存储地址
    print(id(0))


def _sorted():
    # 对集合排序
    print(sorted([3, 1, 2], key=lambda x: x, reverse=False))


def _abs():
    # 获取绝对值
    print(abs(-12))


def _div_mod():
    # 获取余数和整数
    print(divmod(5, 2))


def _pow():
    # 求幂
    print(pow(3, 2))


def _range():
    # 产生列表
    print(range(10))


def _sum():
    # 求和
    print(sum([1, 2, 3]))


def _oct():
    # 获取八进制
    print(oct(11))


def _hex():
    # 获取十六进制
    print(hex(11))


def _chr():
    # 获取ascii码
    print(chr(10))


def _ord():
    # ascii码转整数
    print(ord('a'))


def _bin():
    # 获取二进制
    print(bin(11))


def _format():
    # 格式化字符串
    print(format("i am {0}", "zyp"))


def _max():
    # 返回最大值
    print(max([1, 2, 3]))


def _min():
    # 返回最小值
    print(min([1, 2, 3]))


def _all():
    # 集合中都为真时候为真
    print(all([True, False]))


def _any():
    # 集合中一个为真时候为真
    print(any([True, False]))


def _callable():
    # 检测类是否被实例化
    print(callable(test_func))


def _eval():
    # 运算输入的内容
    print(eval("1+2"))
    print(exec("print('123')"))


def _filter():
    # 内容过滤
    for i in filter(lambda x: x > 10, [1, 2, 3, 4, 5, 19]):
        print(i)
    for i in map(lambda x: x + 10, [1, 2, 3, 4, 5, 19]):
        print(i)


def _content():
    # 返回全局和局部内容
    print(globals())
    print(locals())


def _len():
    # 获取长度
    print(len("123"))


def _zip():
    # 拼接集合
    print(zip([1, 2, 3], [4, 5, 6]))


# +++++++++++++++++++++++++++++++++++++++++++对象+++++++++++++++++++++++++++++++++++++++++++++++++++++


# =============================Function============================
def test_func(name, age=11, home='CHN', *args, **kwargs):
    inner = 'inner'
    print(name, age, home, args, kwargs, inner)


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


# =============================List============================
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


def _count():
    # 统计出现次数
    print(test_list.count('0'))


# =============================Dict============================
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


# =============================Generator============================
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


# =============================Str============================
test_str = str("oHo")


def _get_str():
    # 查找字符出现位置
    print(test_str.find('H', 0, 2))


def _split():
    # 分割字符串
    print(test_str.split('H'))
    print(test_str.partition('H'))


def _check():
    # 检测字符串
    print(test_str.startswith('o'))
    print(test_str.endswith('o'))


def _set_shape():
    # 设置形态
    print(test_str.upper())
    print(test_str.lower())
    print(test_str.title())


def _set_format():
    # 对字符串类型格式化
    print(test_str.center(11, 'a'))
    print(test_str.ljust(11, 'a'))
    print(test_str.rjust(11, 'a'))

    print(test_str.zfill(11))

    print(test_str.lstrip('o'))
    print(test_str.rstrip('o'))
    print(test_str.strip('o'))


def _judgment_str():
    # 判断字符串
    print(test_str.isdigit())
    print(test_str.isalpha())
    print(test_str.isalnum())
    print(test_str.islower())
    print(test_str.isupper())
    print(test_str.istitle())
    print(test_str.isspace())


if __name__ == "__main__":
    # _help()
    pass
