import signal


# TYPE: Built-in module

def sig_fun(signum, frame):
    # 信号处理函数
    print('I received: ', signum, frame)


def _help():
    # 交互界面查看文档，使用help(),退出quit
    pass
    # 功能：处理程序信号


def _signal_type():
    # 信号类型
    # 意义是接受到什么型号，交给那个函数进行处理
    signal.signal(signal.SIGHUP, sig_fun)  # 1
    signal.signal(signal.SIGINT, sig_fun)  # 2  终止进程  中断进程  (control+c)
    signal.signal(signal.SIGQUIT, sig_fun)  # 3  退出进程 和SIGTERM类似
    signal.signal(signal.SIGALRM, sig_fun)  # 14   闹钟信号
    signal.signal(signal.SIGTERM, sig_fun)  # 15   终止进程     软件终止信号
    signal.signal(signal.SIGCONT, sig_fun)  # 18


def _signal():
    # 信号发送方式
    signal.signal(signal.SIGTSTP, sig_fun)
    # 让该进程暂停以等待信号
    signal.pause()
    # 定时给自己发送信号
    signal.alarm(123456)
    print('End of Signal Demo')


if __name__ == "__main__":
    # _help()
    pass
