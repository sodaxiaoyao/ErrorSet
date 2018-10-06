import pip_autoremove


# TYPE: Third-party package

def _help():
    # 交互界面查看文档，使用help(),退出quit
    print(pip_autoremove.__doc__)


def _shell():
    # shell脚本操作指南,自动删除包及其依赖包
    return {
        "-l": "列出无用的包，但是不卸载",
        "-y": "不询问确认",
    }


if __name__ == "__main__":
    # _help()
    pass
