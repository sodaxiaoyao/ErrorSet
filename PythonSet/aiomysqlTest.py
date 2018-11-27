import asyncio
import aiomysql


# TYPE: Third-party package

def _help():
    # 交互界面查看文档，使用help(),退出quit
    pass
    # 功能：异步执行MySQL数据库


async def connect_mysql(my_loop):
    # 连接数据库
    pool = await aiomysql.create_pool(host='', port=62310,
                                      user='root', password='',
                                      db='mysql', loop=my_loop)
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT 42;")
            print(cur.description)
            r = await cur.fetchone()
            print(r)
    pool.close()
    await pool.wait_closed()


def start():
    # 运行连接数据库
    loop = asyncio.get_event_loop()
    loop.run_until_complete(connect_mysql(loop))
    loop.close()


if __name__ == "__main__":
    # _help()
    pass
