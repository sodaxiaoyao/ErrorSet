# TYPE: Built-in syntax


def _help():
    # Python项目命名规则
    naming_rules = {
        "项目": "Word_word",
        "包": "word_word",

        "模块": "wordWord",
        "类": "WordWord",

        "方法": "do_word",
        "函数": "do_word",

        "变量": "word_word",
        "常量": "WORD_WORD",

        "私有": "__word",
        "冲突": "_word",
        "魔法": "__word__"
    }
    naming_rules.update({"填充符": "fill"})


def _bitwise():
    # 60 = 00111100 ,13 = 00001101 : 位运算符
    print(bin(60 & 13).replace("0b", "").zfill(8), ":与")
    print(bin(60 | 13).replace("0b", "").zfill(8), ":或")
    print(bin(60 ^ 13).replace("0b", "").zfill(8), ":异或")
    print(bin(~13).replace("0b", "").zfill(8), ":取反")
    print(bin(13 >> 2).replace("0b", "").zfill(8), ":右移")
    print(bin(13 << 2).replace("0b", "").zfill(8), ":左移")


if __name__ == "__main__":
    _bitwise()
