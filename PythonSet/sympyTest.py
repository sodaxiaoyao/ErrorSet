import sympy


# TYPE: Third-party package

def _help():
    # 交互界面查看文档，使用help(),退出quit
    pass
    # 功能：科学代数计算的工具


def _solve():
    # 解一元一次方程
    x = sympy.Symbol('x')
    print(sympy.solve(x * 3 - 6, x))

    # 解二元一次方程
    # 注：(1)在计算之前要将变量设为符号
    # 　　(2)要将变量一到一侧
    y = sympy.Symbol('y')
    print(sympy.solve([y + x - 1, 3 * x + 2 * y - 5], [x, y]))


def _limit():
    # 求极限
    x = sympy.Symbol('x')
    print(sympy.limit(1 / x ** 2, x, 0))


def _integrate():
    # 求积分
    t = sympy.Symbol('t')
    x = sympy.Symbol('x')
    m = sympy.integrate(sympy.sin(t) / (sympy.pi - t), (t, 0, x))
    n = sympy.integrate(m, (x, 0, sympy.pi))
    print(n)


def _expand():
    # 展开式子
    x = sympy.Symbol('x')
    y = sympy.Symbol('y')
    print(sympy.expand(x * (x + 2 * y)))


def _factor():
    # 合并式子
    x = sympy.Symbol('x')
    y = sympy.Symbol('y')
    print(sympy.factor(x ** 2 + 2 * x * y))


def _cancel():
    # 对函数约分
    x = sympy.Symbol('x')
    print(sympy.cancel((x ** 2 + 2 * x + 1) / (x ** 2 + x)))


def _diff():
    # 求导
    x = sympy.Symbol('x')
    print(sympy.diff(sympy.sin(x) * sympy.exp(x), x))


def _derivative():
    # 定义一个导函数
    x = sympy.Symbol('x')
    print(sympy.Derivative(sympy.sin(x), x))


def _matrix():
    # 求矩阵特征值
    print(sympy.Matrix([[1, 2], [2, 2]]).eigenvals())


def _eq():
    # 创建方程
    x = sympy.Symbol('x')
    print(sympy.solve(sympy.Eq(x + 1, 4), x))


def _simplify():
    # 验证两个方程是否恒等
    x = sympy.Symbol('x')
    a = (x + 1) ** 2
    b = x ** 2 + 2 * x + 1
    print(sympy.simplify(a - b) == 0)


def _rational():
    # 分数表示
    print(sympy.Rational(1, 2))


def _evalf():
    # 小数表示
    expr = sympy.sqrt(8)
    print(expr.evalf(chop=True))


def _collect():
    # 对X合并同类项
    x = sympy.Symbol('x')
    y = sympy.Symbol('y')
    z = sympy.Symbol('z')
    expr = x * y + x - 3 + 2 * x ** 2 - z * x ** 2 + x ** 3
    sympy.collect(expr, x)


def _apart():
    # 拆分代数
    x = sympy.Symbol('x')
    expr = (4 * x ** 3 + 21 * x ** 2 + 10 * x + 12) / (x ** 4 + 5 * x ** 3 + 5 * x ** 2 + 4 * x)
    print(sympy.apart(expr))


def _trigsimp():
    # 简化三角函数
    x = sympy.Symbol('x')
    print(sympy.trigsimp(sympy.sin(x) ** 4 - 2 * sympy.cos(x) ** 2 * sympy.sin(x) ** 2 + sympy.cos(x) ** 4))


def _expand_trig():
    # 展开三角函数
    x = sympy.Symbol('x')
    y = sympy.Symbol('y')
    print(sympy.expand_trig(sympy.sin(x + y)))


def _powsimp():
    # 简化指数运算
    x = sympy.Symbol('x')
    a = sympy.Symbol('a')
    b = sympy.Symbol('b')
    print(sympy.powsimp(x ** a * x ** b))


if __name__ == "__main__":
    # _help()
    pass
