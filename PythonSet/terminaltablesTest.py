import terminaltables

# TYPE: Third-party module

test_table = [
    ['Heading1', 'Heading2'],
    ['row1 column1', 'row1 column2'],
    ['row2 column1', 'row2 column2'],
    ['row3 column1', 'row3 column2'],
]


def _help():
    # 交互界面查看文档，使用help(),退出quit
    pass
    # 功能：以字符串表格方式打印输出内容


def _ascii_table():
    # ascii表格显示
    table = terminaltables.AsciiTable(test_table)
    print(table.table)


if __name__ == "__main__":
    # _help()
    pass
