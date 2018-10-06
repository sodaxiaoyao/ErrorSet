import io


# TYPE: Built-in module


def _help():
    # 交互界面查看文档，使用help(),退出quit
    print(io.__doc__)


def _io_base():
    # IO的最基本类
    return {
        "close()": "冲洗并关闭此流，一旦文件关闭，对文件的任何操作都会引发一次ValueError异常",
        "closed()": "如果流文件被关闭则返回True否则返回False",
        "fileno()": "返回流的底层文件描述符为整数",
        "flush()": "刷新流到写入缓冲区",
        "isatty()": "如果流是交互式即连接到终端设备则返回True否则返回False",
        "readable()": "如果可以从流中读取则返回True否则返回False",
        "readline()": "从流中读取并返回一行，如果size指定，则读取指定大小字节的数据",
        "readlines()": "从流中读取并返回行列表，可以指定hint来控制读取的行数。",
        "seek()": "offset 偏移量，whence 偏移量指示位置",
        "seekable()": "如果流支持随机访问则返回True否则返回false",
        "tell()": "返回当前流的位置",
        "truncate()": "将流大小调整为以字节为单位的给定大小（size），返回新的文件大小",
        "writable()": "如果流支持写入则返回true，否则返回false",
        "writelines()": "写入流列表，不提供换行符",
    }


def _raw_io_base():
    # 二进制IO的最基本类
    return {
        "read()": "从对象中读取size指定大小的字节并返回",
        "readall()": "读取并返回流中的所有字节",
        "readinto()": "将字节读入预先分配的可写类字节对象b，并返回读取的字节数，读取 完返回None",
        "write()": "写入给定类字节对象b，并返回写入字节的数目",
    }


def _bufffered_io_base():
    # 支持缓冲的二进制IO的最基本类
    return {
        "detache()": "将底层原始流从缓冲区分离出来并返回，在原始流被分离后，缓冲区处于不可用状态",
    }


def _string():
    # 字节IO
    fp = io.StringIO("some initial text datal")
    print(fp.getvalue())
    fp.close()
    return {
        "encoding": "用于将流的字节解码为字符串[TextIOBase]",
        "errors": "解码器或编码器的错误设置",
        "newlines": "表示翻译的换行符或一个字符串或一个字符串元祖",
        "buffer": "基本的二进制缓冲区",
        "detach()": "分离底层二进制缓冲区TextIOBase并将其返回,StringIO没有底层缓冲的概念",
        "read()": "从流中读取并返回最多size大小的字符作为单个字符str",
        "readline()": "读取一行或EOF返回一个str",
        "seek()": "改变流位置的偏移量",
        "tell()": "返回当前的流位置",
        "write()": "将字符串s写入流并返回写入的字符数",

        "line_buffering": "线路缓冲是否启用[TextIOWrapper]",

        "getvalue()": "返回一个str包含缓冲区的全部内容，换行符被解码[StringIO]",
    }


def _bytes():
    # 二进制IO
    fp = io.BytesIO(b"some initial binary data:\x00\x01")
    print(fp.getvalue())
    fp.close()
    return {
        "getbuffer()": "在缓冲区的内容上返回一个可读写的试图，另外改变视图将透明的更新缓冲区的内容。[BytesIO]",

        "peek()": "返回流中的字节而不推进位置，对原始流最多进行一次读取。[BufferedReader]",
        "read()": "读取并返回size字节，如果未给出size将直到EOF或读取调用将在非阻塞模式下阻塞。",
        "read1()": "只在原始流上调用一次，返回size字节，否则创建一个原始流读取调用。",

        "write()": "写入字节对象b并返回写入的字节数[BufferedWriter]",
        "flush()": "强制缓冲区中字节流保存到原始流",

        "BufferedRandom": "随机访问流的缓冲接口,继承了BufferedReader和BufferedWriter的所有属性和方法",

        "BufferedRWPair": "继承了BufferedIOBase的所有方法，除了detach()"
    }


def _file():
    # 原始IO,实现了RawIOBase接口和IOBase接口
    return {
        "mode": "在构造函数中给出的模式",
        "name": "文件名称，这是在构造函数中没有给出名称事该文件的文件描述符",
    }


if __name__ == "__main__":
    # _help()
    pass
