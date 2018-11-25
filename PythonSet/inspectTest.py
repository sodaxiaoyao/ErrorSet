import inspect


# TYPE: Built-in module

class TestClass:
    def __init__(self):
        pass


def _help():
    # 交互界面查看文档，使用help(),退出quit
    print(inspect.__doc__)


def _getmembers():
    # 获取对象所有子成员
    print(inspect.getmembers(TestClass))


def _getmodulename():
    # 获取路径下模块的名称
    print(inspect.getmodulename("./inspectTest.py"))


def _ismodule():
    # 判断对象是否是模块
    print(inspect.ismodule(TestClass))


def _isclass():
    # 判断对象是否是类
    print(inspect.isclass(TestClass))


def _isfunction():
    # 判断对象是否是函数
    print(inspect.isfunction(TestClass))


def _isgenerator():
    # 判断对象是否是generator对象
    print(inspect.isgenerator(TestClass))


def _isgeneratorfunction():
    # 判断对象是否是generator函数
    print(inspect.isgeneratorfunction(TestClass))


def _iscoroutine():
    # 判断对象是否是协程
    print(inspect.isfunction(TestClass))


def _iscoroutinefunction():
    # 判断对象是否是协程函数
    print(inspect.iscoroutinefunction(TestClass))


if __name__ == "__main__":
    # _help()
    pass
