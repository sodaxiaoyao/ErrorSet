import argparse


# TYPE: Built-in module

def _help():
    # 交互界面查看文档，使用help(),退出quit
    pass
    # 功能：处理命令行参数


def _create_parser():
    # 创建解释器对象
    parser = argparse.ArgumentParser(description="calculate X to the power of Y")
    return parser


def _add_positional(parser):
    # 添加位置参数
    parser.add_argument("test_str")


def _add_option(parser):
    # 添加操作参数
    group = parser.add_mutually_exclusive_group()
    # 互斥参数组
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")

    parser.add_argument("-SV", "--set_version", help="set version", action="store_true", default='1')
    parser.add_argument("-I", "--number", type=int, help="get number", choices=[0, 1, 2])


def _start_parser(parser):
    # 返回解释器传入内容
    return parser.parse_args()


if __name__ == "__main__":
    # _help()
    pass
