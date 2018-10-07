import setuptools
from setuptools import setup, find_packages


# TYPE: Built-in package

def _help():
    # 交互界面查看文档，使用help(),退出quit
    # 参考地址：http://blog.konghy.cn/2018/04/29/setup-dot-py/
    print(setuptools.__doc__)


def _setup():
    # 基本启动文件
    setup(
        name='MyName',
        version='1.0',
        platforms="Windows",
        description='My module for learn',
        long_description="",

        author='SystemLight',
        author_email='1466335092@qq.com',
        maintainer="SystemLight",
        maintainer_email="1466335092@qq.com",
        url='https://github.com/SystemLight/',
        download_url="https://github.com/SystemLight/",

        requires=[],  # 指定依赖的其他包
        provides=[],  # 指定可以为哪些模块提供依赖
        install_requires=[
            'requests>=1.0',
            'flask>=1.0'
        ],  # 安装时需要安装的依赖包
        dependency_links=[
            "http://packages.example.com/snapshots/foo-1.0.tar.gz",
            "http://example2.com/p/bar-1.0.tar.gz",
        ],  # 指定依赖包的下载地址
        setup_requires=[],  # 指定运行 setup.py 文件本身所依赖的包

        packages=[],
        include_package_data=True,  # 自动包含包内所有受版本控制(cvs/svn/git)的数据文件
        exclude_package_data=[],  # 当 include_package_data 为 True 时该选项用于排除部分文件
        package_data={'my_pkg': ['data/*.dat'], },  # 手动添加包内需要包含的数据文件
        package_dir={'': '.'},  # 指定哪些目录下的文件被映射到哪个源码包
        py_modules=['distutilsTest'],
        data_files=[(".", ".")],  # (目地安装目录，源文件)表示哪些文件被安装到哪些目录中
        scripts=[],  # 如果包中包含执行文件，复制到/usr/local/bin下,安装到PATH
        zip_safe=False,  # 不压缩包，而是以目录的形式安装
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


def _find_packages():
    # 自动查找包
    return find_packages(where='.', exclude=(), include=('*',))


if __name__ == "__main__":
    # _help()
    pass
