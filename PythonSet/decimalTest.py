import decimal


# TYPE: Built-in module

def _help():
    # 交互界面查看文档，使用help(),退出quit
    pass
    # 功能：精度数据处理方法


def _getcontext():
    # 设置全局精度
    decimal.getcontext().prec = 6


def _decimal():
    # 创建对象
    d = decimal.Decimal(1)
    d.from_float(22.222)
    d.quantize(decimal.Decimal('0.00'))  # 设置保留位数


if __name__ == "__main__":
    # _help()
    pass
