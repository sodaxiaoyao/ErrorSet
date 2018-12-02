import os
import os.path


# TYPE: Built-in module

def _help():
    # 交互界面查看文档，使用help(),退出quit
    pass
    # 功能：系统相关处理


# ======================OS=======================
def _listdir():
    # 获取指定目录下的文件及文件夹名称
    print(os.listdir('.'))


def _walk():
    # 遍历目录
    print(os.walk("."))


def _kill():
    # 杀死进程
    os.kill(123, 123)  # pid , sid
    os.killpg(123, 123)  # pgid , sid


def _u_time():
    # 指定路径文件最后的修改和访问时间[访问|修改]
    os.utime("a.py", (1330712280, 1330712292))


def _stat():
    # 获取文件信息
    print(os.stat("./timeTest.py"))
    # st_mode: i_node 保护模式
    # st_ino: i_node 节点号。
    # st_dev: i_node 驻留的设备。
    # st_n_link: i_node 的链接数。
    # st_uid: 所有者的用户ID。
    # st_gid: 所有者的组ID。
    # st_size: 普通文件以字节为单位的大小；包含等待某些特殊文件的数据。
    # st_a_time: 上次访问的时间。
    # st_m_time: 最后一次修改的时间。
    # st_c_time: 由操作系统报告的"c_time"。


def _open():
    # 打开文件
    """
        os.O_RDONLY: 以只读的方式打开
        os.O_WRONLY: 以只写的方式打开
        os.O_RDWR : 以读写的方式打开
        os.O_NONBLOCK: 打开时不阻塞
        os.O_APPEND: 以追加的方式打开
        os.O_CREAT: 创建并打开一个新文件
        os.O_TRUNC: 打开一个文件并截断它的长度为零（必须有写权限）
        os.O_EXCL: 如果指定的文件存在，返回错误
        os.O_SHLOCK: 自动获取共享锁
        os.O_EXLOCK: 自动获取独立锁
        os.O_DIRECT: 消除或减少缓存效果
        os.O_FSYNC : 同步写入
        os.O_NOFOLLOW: 不追踪软链接
     """
    return os.open("./timeTest", flags=os.O_RDONLY)


def _read(fd):
    # 读取fd[文件描述符，读取字节数]
    os.read(fd, 12)


def _write(fd):
    # 写内容
    os.write(fd, bytes("zyp", 'UTF-8'))


def _close(fd):
    # 关闭打开的文件
    os.close(fd)


def _get_cwd():
    # 获取当前目录
    print(os.getcwd())


def _ch_dir():
    # 更换当前目录
    os.chdir(".")


def _rename():
    # 更换文件名称
    os.rename('c.txt', 'a.txt')


def _renames():
    # 更换文件名称,递归
    os.renames('c.txt', 'a.txt')


def _mkdir():
    # 创建新目录
    os.mkdir('新目录')


def _rmdir():
    # 删除空文件夹
    os.rmdir('新目录')


def _make_dirs():
    # 以此创建目录
    os.makedirs('E:\\xixi\\haha')


def _removedirs():
    # 以此删除空目录
    os.removedirs('E:\\xixi\\haha')


def _remove():
    # 删除文件
    os.remove("./a.py")


def _sep():
    # 获取当前操作系统的路径分隔符
    print(os.sep)


def _environ():
    # 获取当前操作系统的环境变量
    print(os.environ)


def _path_sep():
    # 获取当前系统的环境变量中每个路径的分隔符
    print(os.pathsep)


def _system():
    # shell命令
    os.system("echo 'zyp'")
    print(os.popen("echo 'zyp'").read())


def _unlink():
    # 删除文件, 如果文件是一个目录则返回一个错误。
    os.unlink("")


# ======================OS_PATH=======================
def _abspath():
    # 获取当前文件的绝对路径
    print(os.path.abspath(__file__))


def _dir_name():
    # 获取指定路径的父目录
    print(os.path.dirname(os.path.abspath(__file__)))


def _base_name():
    # 获取目录下名字
    os.path.basename("/etc/sysconfig/zyp")


def _samefile():
    # 判断目录或文件是否相同
    os.path.samefile("/etc/sysconfig/zyp", "/etc/sysconfig/zyp")


def _isdir():
    # 判断指定路径是不是一个文件夹
    print(os.path.isdir(os.path.abspath(__file__)))


def _getsize():
    # 获取文件大小
    print(os.path.getsize("./a.py"))


def _isfile():
    # 判断指定路径是不是一个文件夹
    print(os.path.isfile(os.path.abspath(__file__)))


def _join():
    #  将内容以当前操作系统的路径分隔符拼接成一个路径
    print(os.path.join('一级', '二级', '三级', 'haha.txt'))


def _split():
    # 分割路径和文件名
    print(os.path.split('E:\study\Automantic\jxz-code\Course4\函数.py'))


def _exists():
    # 判断目录或文件是否存在
    print(os.path.exists('E:\study\Automantic\jxz-code\Course4\函数.py'))


def _splitext():
    # 分离文件名和拓展名
    os.path.splitext("a.txt")


def _norm():
    # 规范分割符号
    os.path.normpath('E:\study\Automantic\jxz-code\Course4\函数.py')


def _expandvars():
    # 自动替换环境变量中的内容
    print(os.path.expandvars("Tmp path is ${tmp}"))


def _expanduser():
    # 把path中包含的"~"和"~user"转换成用户目录
    print(os.path.expanduser("~"))


if __name__ == "__main__":
    # _help()
    pass
