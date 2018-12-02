import subprocess


# TYPE: Built-in module

def _help():
    # 交互界面查看文档，使用help(),退出quit
    pass
    # 功能：管道子进程控制


def _run():
    # 执行指定的命令，等待命令执行完成后返回一个包含执行结果的CompletedProcess类的实例
    completed_process = subprocess.run(["dir", "d:\\"], input=None, stdin=None,
                                       stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                       timeout=None, shell=True, check=False, universal_newlines=False)
    print(completed_process.args)
    print(completed_process.returncode)
    print(completed_process.stdout)
    print(completed_process.stderr)
    print(completed_process.check_returncode())


def _call():
    # 执行指定的命令，返回命令执行状态，其功能类似于os.system(cmd)。
    subprocess.call(['dir', 'd:\\'], shell=True)


def _check_call():
    # 执行指定的命令，如果执行成功则返回状态码，否则抛出异常
    subprocess.check_call(['dir', 'd:\\'], shell=True)


def _check_output():
    # 执行指定的命令，如果执行状态码为0则返回命令执行结果，否则抛出异常
    subprocess.check_output(['dir', 'd:\\'], shell=True)


def _getoutput():
    # 接收字符串格式的命令，执行命令并返回执行结果
    subprocess.getoutput("dir")


def _getstatusoutput():
    # 执行cmd命令，返回一个元组(命令执行状态, 命令执行结果输出)
    subprocess.getstatusoutput("dir")


def _popen():
    # 底层的内容
    p = subprocess.Popen('dir', stdout=subprocess.PIPE, shell=True)

    print(p.stdout.read())
    p.stdin.write('print(1) \n')
    out, err = p.communicate(input=None, timeout=None)
    print(out, err)

    # 用于检查子进程（命令）是否已经执行结束，没结束返回None，结束后返回状态码
    print(p.poll())
    p.wait(timeout=None)

    # p.send_signal(signal.SIGINT)
    p.terminate()
    p.kill()


if __name__ == "__main__":
    # _help()
    pass
