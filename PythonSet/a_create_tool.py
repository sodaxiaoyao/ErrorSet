import os.path

name = input("请输入模块：")
module_name = name

name = "{}Test.py".format(name)
print(name)
if not os.path.exists(name):
    with open(name, 'w', encoding="utf8") as fp:
        the_type = input("输入数字（内置模块1，第三方模块2，内置包3，第三方包4）：")
        flag = False
        content = """import re


# TYPE: source s_type

def _help():
    # 交互界面查看文档，使用help(),退出quit
    pass
    # 功能：


def _example():
    # 例子
    pass


if __name__ == "__main__":
    # _help()
    pass
"""

        if str(the_type) == '1':
            content = content.replace("source", "Built-in").replace("s_type", "module")
        elif str(the_type) == '2':
            content = content.replace("source", "Third-party").replace("s_type", "module")
        elif str(the_type) == '3':
            content = content.replace("source", "Built-in").replace("s_type", "package")
        elif str(the_type) == '4':
            content = content.replace("source", "Third-party").replace("s_type", "package")
        else:
            print("输入错误")
            flag = True

        if not flag:
            print(name + "被创建")
            fp.write(content.replace("re", module_name))

    if flag:
        os.remove(name)

else:
    print("已经存在")
