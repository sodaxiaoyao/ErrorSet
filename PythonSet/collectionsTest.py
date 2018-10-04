import collections


# TYPE: Built-in package

def _help():
    # 内置对结合操作的包
    pass


def _namedtuple():
    # 创建一个自定义的元组对象
    return collections.namedtuple('MyTuple', ['x', 'y'])


def _deque():
    # 高效实现插入和删除操作的双向列表
    my_list = collections.deque(['a', 'b', 'c'])

    my_list.append('e')
    my_list.appendleft('e')

    my_list.pop()
    my_list.popleft()


def _default_dict():
    # 如果希望key不存在时，返回一个默认值
    my_dict = collections.defaultdict(lambda: 'N/A')
    my_dict['key1'] = 'abc'


def _order_dict():
    # 有序字典
    return collections.OrderedDict([('a', 1), ('b', 2), ('c', 3)])


def _counter():
    # 计数器
    return collections.Counter()


if __name__ == "__main__":
    # _help()
    pass
