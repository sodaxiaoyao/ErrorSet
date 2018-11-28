import pymysql


# TYPE: Third-party package

def _help():
    # 交互界面查看文档，使用help(),退出quit
    pass
    # 功能：连接MySQL数据库


def _mysql():
    # 创建连接对象
    conn = pymysql.connect(host="192.168.2.3", db="book", user="root", password="1qaz@WSX", port=3306, charset='utf8')
    # 获取游标
    cur = conn.cursor()
    print(cur.lastrowid)  # 获取自增ID
    cur.scroll(1, mode='relative')  # 相对当前位置移动,移动游标
    cur.scroll(2, mode='absolute')  # 绝对位置移动,移动游标

    # 游标设置为字典类型
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 无参数存储过程
    cursor.callproc('p2')  # 等价于cursor.execute("call p2()")
    # 有参数存储过程
    cursor.callproc('p1', args=(1, 22, 3, 4))
    return cur, conn


def _select(cur, conn):
    # 查询对象
    try:
        cur.execute("")  # 执行sql语句
        print("id", "name", "password")
        # cur.fetchone()
        # cur.fetchmany(2)
        for row in cur.fetchall():
            print(row[0], row[1], row[2])
    except Exception as e:
        raise e
    finally:
        conn.close()


def _update(cur, conn):
    # 更改对象
    try:
        cur.execute("")
        # cur.executemany("",[])
        # 提交
        conn.commit()
    except Exception as e:
        # 错误回滚
        print(e)
        conn.rollback()
    finally:
        conn.close()


if __name__ == "__main__":
    # _help()
    pass
