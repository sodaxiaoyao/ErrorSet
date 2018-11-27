import queue


# TYPE: Built-in module


def _help():
    # 交互界面查看文档，使用help(),退出quit
    pass
    # 功能：队列对象


def _queue():
    # 创建队列
    return [
        queue.Queue(maxsize=0),
        queue.LifoQueue(maxsize=0),
        queue.PriorityQueue(maxsize=0)
    ]
    # 使用PriorityQueue，对象必须实现__cmp__


def _option(q: queue.Queue):
    # 提取和上传队列
    q.put("s")
    q.get()


def _empty(q: queue.Queue):
    # 判断队列是否为空
    q.empty()


def _join(q: queue.Queue):
    # 阻塞调用，知道全部任务完成
    q.join()


def _task_done(q: queue.Queue):
    # 告诉队列任务处理完成
    q.task_done()


if __name__ == "__main__":
    # _help()
    pass
