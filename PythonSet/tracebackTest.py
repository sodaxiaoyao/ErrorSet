import traceback


# TYPE: Built-in module

def _help():
    # 交互界面查看文档，使用help(),退出quit
    pass
    # 功能：异常处理，放入文件


def _print_exc():
    # 直接打印，或者放入文件
	try:
		raise SyntaxError, "traceback test"
	except:
		traceback.print_exc(file=open("1.txt","a+"))
    
	
def _print_exc():
    # 返回错误信息字符串
	try:
		raise SyntaxError, "traceback test"
	except:
		traceback.format_exc()


if __name__ == "__main__":
    # _help()
    pass
