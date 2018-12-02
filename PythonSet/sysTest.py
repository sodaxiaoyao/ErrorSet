import sys


# TYPE: Built-in module

def _help():
    # 交互界面查看文档，使用help(),退出quit
    pass
    # 功能：系统功能模块


def _argv():
    # 获取传递进来的参数
    print(sys.argv)


def _exit():
    # 程序终止
    sys.exit(0)


def _coding():
    # 例子
    print(sys.getdefaultencoding())
    # sys.setdefaultencoding('utf8') # 使用前先reload(sys)
    print(sys.getfilesystemencoding)


def _path():
    # 获取模块搜索路径
    print(sys.path)


def _platform():
    # 获取当前系统平台
    print(sys.platform)


def _out_in():
    # 标准输入和输出
    the_in = sys.stdin
    sys.stdout = the_in
    sys.stderr = the_in


def _modules():
    # 查询模块位置信息
    print(sys.modules["module_name"])


if __name__ == "__main__":
    # _help()
    pass
