import tempfile


# TYPE: Built-in module

def _help():
    # 交互界面查看文档，使用help(),退出quit
    pass
    # 功能：获取操作系统临时文件


def _mkstemp():
    # 创建临时文件
    tmpfd, tempfilename = tempfile.mkstemp(suffix="", prefix="", dir=None, text=False)
    print(tmpfd)
    import os
    os.close(tmpfd)


def _mkdtemp():
    # 创建临时文件夹
    path = tempfile.mkdtemp(suffix="", prefix="", dir=None)
    print(path)


def _mktemp():
    # mktemp用于返回一个临时文件的路径，但并不创建该临时文件。
    path = tempfile.mktemp(suffix="", prefix="", dir=None)
    print(path)


def _tempdir():
    # 该属性用于指定创建的临时文件（夹）所在的默认文件夹
    tempfile.tempdir = "./"


def _gettempdir():
    # 用于返回保存临时文件的文件夹路径。
    print(tempfile.gettempdir())


def _immediate():
    # 随关随删文件
    obj_tmp = tempfile.TemporaryFile(mode='w+b', buffering=-1, encoding=None,
                                     newline=None, suffix=None, prefix=None,
                                     dir=None)
    # 当delete = True的时候，行为与TemporaryFile一样
    obj_tmp_2 = tempfile.NamedTemporaryFile(mode='w+b', buffering=-1, encoding=None,
                                            newline=None, suffix=None, prefix=None,
                                            dir=None, delete=True)
    # 向类文件对象写数据的时候，数据长度只有到达参数max_size指定大小时，或者调用类文件对象的fileno()
    # 方法，数据才会真正写入到磁盘的临时文件中
    obj_tmp_3 = tempfile.SpooledTemporaryFile(max_size=1000, mode='w+b', buffering=-1,
                                              encoding=None, newline=None,
                                              suffix=None, prefix=None, dir=None)
    print(obj_tmp, obj_tmp_2, obj_tmp_3)


if __name__ == "__main__":
    # _help()
    pass
