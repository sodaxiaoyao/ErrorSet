import struct


# TYPE: Built-in module

def _help():
    # 交互界面查看文档，使用help(),退出quit
    pass
    # 功能：网络传递int、char之类的基本数据


def _pack():
    # 打包和解包
    s = struct.Struct('I3sf')
    print('Format string :', s.format)
    print('Uses :', s.size, 'bytes')

    packed_data = s.pack(*(1, b'abc', 2.7))
    unpacked_data = s.unpack(packed_data)

    print('Packed Value :', packed_data)
    print('Unpacked Type :', type(unpacked_data), ' Value:', unpacked_data)

    # 传递类型
    # I  integer
    # f  float
    # s  bytes
    # ?  bool
    # q  long
    # d  double

    # 字节顺序
    # @ < > = !


if __name__ == "__main__":
    # _help()
    pass
