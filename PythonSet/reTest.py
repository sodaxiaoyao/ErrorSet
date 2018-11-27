import re

# TYPE: Built-in module

test_str = "i am zyp i am"


def _help():
    # 交互界面查看文档，使用help(),退出quit
    pass
    # 功能：正则表达式


def _flags():
    # 正则表达式标识符
    print({
        re.S: "使.匹配包括换行在内的所有字符",
        re.I: "使匹配对大小写不敏感",
        re.U: "根据Unicode字符集解析字符，这个标志影响\w,\W,\b,\B",
        re.M: "多行匹配，影响^和$",
        re.L: "做本地化识别（locale-aware)匹配，法语等",
        re.X: "该标志通过给予更灵活的格式以便将正则表达式写得更易于理解",
    })


def _compile():
    # 编译正则表达式
    print(re.compile(r'am', flags=0))


def _match():
    # 从匹配字符串开头开始匹配第一个
    print(re.match("(i) (am)", test_str, flags=0).groups())


def _search():
    # 从匹配字符串中开始匹配第一个
    print(re.search("(i) (am)", test_str).groups())

    # match_object对象的方法：
    #   group() 返回被 RE 匹配的字符串
    #   groups() 方法返回一个包含正则表达式中所有小组字符串的元组
    #   span() 返回一个元组包含匹配 (开始,结束) 的位置
    #   start() 返回匹配开始的位置
    #   end() 返回匹配结束的位置


def _findall():
    # 从匹配字符串中匹配所有字符串
    print(re.findall("(i) (am)", test_str))


def _finditer():
    # 从匹配字符串中匹配所有字符串,返回可迭代对象
    find_iter = re.finditer(r'i', test_str)
    for i in find_iter:
        print(i.group())


def _split():
    # 按照匹配字符进行分割
    print(re.split(" ", test_str))


def _sub():
    # 把匹配字符进行替换
    print(re.sub(" ", lambda m: '[' + m.group(0) + ']', test_str, 0))


def _subn():
    # 把匹配字符进行替换，并返回替换总数
    print(re.subn(" ", lambda m: '[' + m.group(0) + ']', test_str, 0))


def _group():
    # 引用分组
    print(re.sub("(?P<the_i>i) (am) (?P<the_zyp>zyp) (?P=the_i)", "\g<the_zyp>", test_str))
    print(re.sub("(i) (am) (zyp)", "\g<2>", test_str))
    print(re.sub(re.compile(r'(hello) \1'), "a", "hello hello"))
    # 忽略分组
    print(re.findall(re.compile(r'(\w)\1(?:\w)\1'), "abab cdcd xxyx"))


def _grammar():
    # 匹配的特殊字符
    print({
        "\cx": "x 的值必须为 A-Z 或 a-z 之一,匹配由x指明的控制字符",
        "\f": "匹配一个换页符。等价于 \x0c 和 \cL。",
        "\n": "匹配一个换行符。等价于 \x0a 和 \cJ。",
        "\r": "匹配一个换行符。等价于 \x0a 和 \cJ。",
        "\t": "匹配一个制表符。等价于 \x09 和 \cI。",
        "\v": "匹配一个垂直制表符。等价于 \x0b 和 \cK。",

        "\s": "配任何空白字符，包括空格、制表符、换页符 等价于[\f\n\r\t\v]注意 Unicode 正则表达式会匹配全角空格符",
        "\S": "匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。",
        "\\b": "匹配一个字边界，即字与空格间的位置。",
        "\B": "非字边界匹配",

        "\d": "匹配一个数字字符",
        "\D": "匹配一个非数字字符",
        "\w": "匹配字母、数字、下划线。等价于'[A-Za-z0-9_]'。",
        "\W": "匹配非字母、数字、下划线。等价于 '[^A-Za-z0-9_]'。",

        "$": "结尾",
        "^": "开始",
        ".": "	匹配除换行符 \n 之外的任何单字符",
        "*": "前面的0或n次[限定符]",
        "+": "前面的1或n次[限定符]",
        "?": "匹配前面的子表达式零次或一次，或【紧跟跟随其他限定符】指明一个非贪婪限定符[限定符]",
        "|": "或者",

        "[]": "中括号表达式",
        "{n,m}": "大括号表达式,n到m次[限定符]",
        "( )": "子表达式，分组",

        "(?:pattern)": "忽略分组",

        "(?=pattern)": "正向肯定预查,匹配表达式前面的内容，表达式不参与匹配，匹配的所有内容，按表达式子二次筛选",
        "(?!pattern)": "正向否定预查(negative assert)",
        "(?<=pattern)": "反向(look behind)肯定预查",
        "(?<!pattern)": "反向否定预查",
    })


if __name__ == "__main__":
    # _help()
    pass
