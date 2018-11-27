import chardet


# TYPE: Third-party package

def _help():
    # 交互界面查看文档，使用help(),退出quit
    pass
    # 功能：判断字符编码的类型


def _detect():
    # 获取编码
    print(chardet.detect(b'Hello, world!'))
    print(chardet.detect('离离原上草，一岁一枯荣'.encode("utf-8")))
    print(chardet.detect('离离原上草，一岁一枯荣'.encode("gbk")))
    print(chardet.detect('最新の主要ニュース'.encode('euc-jp')))


if __name__ == "__main__":
    # _help()
    pass
