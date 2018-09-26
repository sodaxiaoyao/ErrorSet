# TYPE: 命名规则

if __name__ == "__main__":
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
