import fractions


# TYPE: Built-in module

def _help():
    # 交互界面查看文档，使用help(),退出quit
    print(fractions.__doc__)


def _fraction():
    # 自动进行化简（约分）和通分
    f = fractions.Fraction('3/6')
    print(f.from_float(0.5))
    print(f.denominator)
    print(f.numerator)
    # 查找并返回最接近分母
    f.limit_denominator(10)
    return fractions.Fraction(3, 6)


if __name__ == "__main__":
    # _help()
    pass
