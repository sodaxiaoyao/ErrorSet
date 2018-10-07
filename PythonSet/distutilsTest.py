import distutils
from distutils import core


# TYPE: Built-in package

def _help():
    # 交互界面查看文档，使用help(),退出quit
    print(distutils.__doc__)


def _setup():
    # 基本启动文件
    core.setup(
        name='MyName',
        version='1.0',
        platforms="Windows",
        description='My module for learn',

        author='SystemLight',
        author_email='1466335092@qq.com',
        url='https://github.com/SystemLight/',

        packages=[],
        py_modules=['distutilsTest'],
    )


def install_gen():
    # 安装和生成的脚本命令
    return {
        "python setup.py sdist": "生成压缩格式",
        "python setup.py build": "单纯的只构建",
        "python setup.py bdist_wininst": "生成windows可执行文件",
        "python setup.py bdist_rpm": "生成linux可执行文件rpm",
        "python setup.py bdist --help-formats": "查看bdist可构建的格式",

        "python setup.py install": "安装"
    }


if __name__ == "__main__":
    # _help()
    pass
