import dis


# TYPE: Built-in module

def test_func():
    x = 1
    if x < 3:
        return "yes"
    else:
        return "no"


def _help():
    # 交互界面查看文档，使用help(),退出quit
    pass
    # 功能：代码反编译


def _dis():
    # 反编译
    dis.dis(test_func)
    # 第一列：源代码的行数
    # 第二列：字节码的索引
    # 第二列：指令本身对应的人类可读的名字
    # 第四列：表示指令的参数
    # 第五列：计算后的实际参数


if __name__ == "__main__":
    # _help()
    pass
