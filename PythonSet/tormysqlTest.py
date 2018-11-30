import tormysql
from tornado import gen
from tornado.ioloop import IOLoop


# TYPE: Third-party package

def _help():
    # 交互界面查看文档，使用help(),退出quit
    pass
    # 功能：tornado的mysql驱动


@gen.coroutine
def _conn():
    # 创建异步连接
    pool = tormysql.ConnectionPool(
        max_connections=20,  # max open connections
        idle_seconds=7200,  # connection idle timeout time, 0 is not timeout
        wait_connection_timeout=3,  # wait connection timeout
        host="127.0.0.1",
        user="root",
        passwd="TEST",
        db="test",
        charset="utf8"
    )
    with (yield pool.Connection()) as conn:
        try:
            with conn.cursor() as cursor:
                yield cursor.execute("INSERT INTO test(id) VALUES(1)")
        except Exception as e:
            print(e)
            yield conn.rollback()
        else:
            yield conn.commit()

        with conn.cursor() as cursor:
            yield cursor.execute("SELECT * FROM test")
            data = cursor.fetchall()
    print(data)
    yield pool.close()


def _run(conn):
    # 加入队列
    il = IOLoop.instance()
    il.run_sync(conn)


if __name__ == "__main__":
    # _help()
    pass
