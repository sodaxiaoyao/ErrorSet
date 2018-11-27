import importlib
import importlib.util


# TYPE: Built-in module


def _help():
    # 交互界面查看文档，使用help(),退出quit
    pass
    # 功能：动态导入工具包


def _import_module():
    # 导入foo模块调用main方法
    importlib.import_module('foo').main()


def _find_spec():
    # 检查传入的字符串作为模块是否存在
    module_spec = importlib.util.find_spec('bar')
    module = importlib.util.module_from_spec(module_spec)
    # module_from_spec函数，它将会返回引入的模块
    module_spec.loader.exec_module(module)
    # 引入模块后执行它


def _spec_from_file_location(module_name):
    # 通过模块名字和路径导入
    module_file_path = module_name.__file__
    module_name = module_name.__name__

    module_spec = importlib.util.spec_from_file_location(module_name, module_file_path)
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    print(dir(module))
    msg = "The {module_name} module has the following methods:{methods}"
    print(msg.format(module_name=module_name, methods=dir(module)))


if __name__ == "__main__":
    # _help()
    pass
