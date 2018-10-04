from apscheduler.schedulers.blocking import BlockingScheduler


# TYPE: Third-party package

def test_job():
    print("执行任务")


def _help():
    # 第三方的定时任务调度器
    pass


def start_job():
    # 开始执行任务
    scheduler = BlockingScheduler()
    # 类型：``date``, ``interval`` or ``cron``
    job = scheduler.add_job(test_job, 'interval', seconds=3)
    job.remove()
    job.pause()
    job.resume()
    scheduler.start()
    scheduler.pause()
    scheduler.resume()
    scheduler.shutdown(wait=True)

    # 按照日期
    # scheduler.add_job(my_job, 'date', run_date=date(2017, 9, 8), args=[])
    # scheduler.add_job(my_job, 'date', run_date=datetime(2017, 9, 8, 21, 30, 5), args=[])
    # scheduler.add_job(my_job, 'date', run_date='2017-9-08 21:30:05', args=[])

    # 按照间隔
    # scheduler.add_job(my_job, 'interval', hours=2)
    # scheduler.add_job(my_job, 'interval', hours=2, start_date='2017-9-8 21:30:00', end_date='2018-06-15 21:30:00)

    # 按照cron语法
    # scheduler.add_job(my_job, 'cron', hour=3, minute=30)
    # scheduler.add_job(my_job, 'cron', day_of_week='mon-fri', hour=5, minute=30, end_date='2017-10-30')

    # 调度器类型
    # BlockingScheduler：只运行调度器
    # BackgroundScheduler: 不想使用任何框架时的方式
    # AsyncIOScheduler: 异步 module的方式（Python3）
    # G_eventScheduler: g_event方式
    # TornadoScheduler: Tornado方式
    # TwistedScheduler: Twisted方式
    # QtScheduler: Qt方式

    # executors组件
    # base|debug|gevent|pool(max_workers=10)|twisted

    # jobstore类型
    # base|memory|mongodb|redis|rethinkdb|sqlalchemy|zookeeper


if __name__ == "__main__":
    # _help()
    pass
