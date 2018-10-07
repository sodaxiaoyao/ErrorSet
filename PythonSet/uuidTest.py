import uuid


# TYPE: Built-in module


def _help():
    # 交互界面查看文档，使用help(),退出quit
    print(uuid.__doc__)


def _create():
    # 创建唯一ID
    print(uuid.uuid1())
    print(uuid.uuid3(uuid.NAMESPACE_DNS, '变换值'))
    print(uuid.uuid5(uuid.NAMESPACE_DNS, '变换值'))


if __name__ == "__main__":
    # _help()
    _create()
    pass
