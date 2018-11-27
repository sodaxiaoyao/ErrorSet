import platform


# TYPE: Built-in module


def _help():
    # 交互界面查看文档，使用help(),退出quit
    pass
    # 功能：平台信息


def _architecture():
    # 系统架构
    print(platform.architecture())


def _system():
    # 系统架构
    print(platform.system())


def _version():
    # 系统版本
    print(platform.version())


def _machine():
    # CPU平台
    print(platform.machine())


def _node():
    # 机器名称
    print(platform.node())


def _u_name():
    # 系统信息
    print(platform.uname())


def _python_version():
    # python版本
    print(platform.python_version())


if __name__ == "__main__":
    # _help()
    pass
