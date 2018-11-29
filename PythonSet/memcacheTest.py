import memcache


# TYPE: Third-party package

def _help():
    # 交互界面查看文档，使用help(),退出quit
    pass
    # 功能：连接memcache缓存数据库NoSql【包：python-memcached】


def _client():
    # 创建连接对象
    mc = memcache.Client(['192.168.2.3:11211'], debug=True)
    return mc


def _store(mc):
    # 基本存储和获取内容
    mc.set("name", "python")
    mc.set_multi({'name': 'to,', 'age': '19', 'job': 'IT'})  # 设置多个键值
    mc.get('name')
    mc.get_multi(['name'])


def _update(mc):
    # 更改数据内容
    mc.delete('name')
    mc.delete_multi(['name'])


def _advance_store(mc):
    # 高级存储
    mc.add('k1', 'v1')  # 累加，已存在返回错误信息
    mc.replace('name', 'jack')  # 如果不存在key，修改失败，返回空值
    mc.prepend('num', '追加前面')
    mc.append('num', '追加后面')
    mc.decr('num', '9')  # 将值增加n
    mc.incr('num', '9')  # 将值减小n
    # 多用户安全读取
    mc.cas("name", "python")
    mc.gets("name")


if __name__ == "__main__":
    # _help()
    pass
