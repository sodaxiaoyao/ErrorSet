import binascii


# TYPE: Built-in module

def _help():
    # 交互界面查看文档，使用help(),退出quit
    pass
    # 功能：二进制和ASCII之间的转换


def _a2b_hex():
    # 16进制byte数据转ascii数据
    print(binascii.a2b_hex(b'7a'))
    print(binascii.unhexlify(b'7a'))


def _b2a_hex():
    # ascii数据转16进制byte数据
    print(binascii.b2a_hex('z'.encode("utf-8")))
    print(binascii.hexlify('z'.encode("utf-8")))


def _a2b_base64():
    # base64的byte数据转ascii数据
    print(binascii.a2b_base64(b'eg==\n'))


def _b2a_base64():
    # ascii数据转base64进制byte数据
    print(binascii.b2a_base64('z'.encode("utf-8")))


def _crc32():
    # 循环冗余校验
    print('0x%x' % (binascii.crc32('zyp'.encode("utf-8")) & 0xffffffff))


if __name__ == "__main__":
    # _help()
    pass
