import pip
from pip._internal import pep425tags


# TYPE: Third-party package

def _help():
    # 交互界面查看文档，使用help(),退出quit
    print(pip.__doc__)


def _shell():
    # shell脚本操作指南
    return {
        "install": "安装包",
        "uninstall": "卸载包",
        "freeze": "按照一定格式输出已安装包列表",
        "list": "列出已安装包",
        "show": "显示包详细信息",
        "search": "搜索包",
        "wheel": "下载wheel文件",
        "help": "帮助",
    }


def _get_supported():
    # 获取支持的版本
    print(pep425tags.get_supported())


if __name__ == "__main__":
    # _help()
    pass
