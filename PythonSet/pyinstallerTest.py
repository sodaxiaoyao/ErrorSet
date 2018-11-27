import PyInstaller


# TYPE: Third-party package

def _help():
    # 交互界面查看文档，使用help(),退出quit
    pass
    # 功能：打包可执行文件的工具


def _create():
    # 创建的文件只支持UTF-8编码格式
    return {
        "pyinstaller 文件名称": "基本创建",
        "-h": "查看帮助",
        "-F": "生成单个可执行文件",
        "-w": "去掉控制台界面，没有GUI的时候不要使用",
        "-i='path'": "可执行文件的图标"
    }


if __name__ == "__main__":
    # _help()
    pass
