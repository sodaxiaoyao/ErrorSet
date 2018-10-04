from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from concurrent.futures import as_completed, wait, FIRST_COMPLETED


# TYPE: Built-in package

def test_gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            print(i)
            return i


def _help():
    # 内置对线程和进程的更抽象实现
    pass


def _thread():
    # 线程：基本创建
    numbers = [
        (1963309, 2265973), (1879675, 2493670), (2030677, 3814172),
        (1551645, 2229620), (1988912, 4736670), (2198964, 7876293)
    ]
    # 创建一个线程池
    pool = ThreadPoolExecutor(max_workers=4)

    # 加入一组任务
    # pool.map(test_gcd, numbers)

    # 往线程池加入2个task
    f1 = pool.submit(test_gcd, numbers[0])
    f2 = pool.submit(test_gcd, numbers[1])

    # 判断任务是否完成
    print(f1.done())
    print(f2.done())

    # 获取任务返回结果
    print(f1.result())
    print(f2.result())


def _as_completed():
    # 线程：获取正在运行和完成的任务Future
    numbers = [
        (1963309, 2265973), (1879675, 2493670), (2030677, 3814172),
        (1551645, 2229620), (1988912, 4736670), (2198964, 7876293)
    ]

    # 创建线程池
    with ThreadPoolExecutor(max_workers=4) as executor:
        future_tasks = [executor.submit(test_gcd, url) for url in numbers]

        # 打印正在运行的任务
        for f in future_tasks:
            print(f)
            if f.running():
                print('%s is running' % str(f))

        # 获取完成和未完成的任务
        completed, uncompleted = wait(future_tasks, timeout=1, return_when=FIRST_COMPLETED)
        print(completed)
        print(uncompleted)

        # 遍历已经完成的任务
        for f in as_completed(future_tasks):
            try:
                ret = f.done()
                if ret:
                    f_ret = f.result()
                    print('%s, done, result: %s' % (f, f_ret))
            except Exception as e:
                # 取消任务
                f.cancel()
                print(e)


def _process():
    # 进程：基本创建
    numbers = [
        (1963309, 2265973), (1879675, 2493670), (2030677, 3814172),
        (1551645, 2229620), (1988912, 4736670), (2198964, 7876293)
    ]
    pool = ProcessPoolExecutor(max_workers=4)

    # 加入一组任务
    # pool.map(test_gcd, numbers)

    # 往线程池加入2个task
    f1 = pool.submit(test_gcd, numbers[0])
    f2 = pool.submit(test_gcd, numbers[1])

    # 判断任务是否完成
    print(f1.done())
    print(f2.done())

    # 获取任务返回结果
    print(f1.result())
    print(f2.result())


if __name__ == "__main__":
    # _help()
    pass
