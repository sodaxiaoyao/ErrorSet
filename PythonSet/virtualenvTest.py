# TYPE: Third-party package


def _help():
    # 第三方的虚拟环境
    # pip3 install virtualenv
    pass


def _create_v():
    # 创建虚拟环境
    return {
        "virtualenv venv": "创建名称是venv的虚拟环境",
        "source venv/bin/activate": "进入虚拟环境",
        "deactivate ": "退出虚拟环境",

        "-h": "查看帮助",
        "--version": "查询版本",
        "--no-site-packages": "不导入第三方包",
    }


if __name__ == "__main__":
    # _help()
    pass
