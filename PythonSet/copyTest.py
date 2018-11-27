import copy

# TYPE: Built-in module
test_obj = 's'


def _help():
    # 交互界面查看文档，使用help(),退出quit
    pass
    # 功能：内容复制


def _copy():
    # 浅拷贝，不会复制子内容
    copy.copy(test_obj)


def _deepcopy():
    # 深拷贝，会复制子内容
    copy.deepcopy(test_obj)


if __name__ == "__main__":
    # _help()
    pass
