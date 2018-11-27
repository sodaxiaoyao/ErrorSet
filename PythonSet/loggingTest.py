import logging
import logging.handlers


# TYPE: Built-in module

def _help():
    # 交互界面查看文档，使用help(),退出quit
    pass
    # 功能：日志工具


def _flags():
    # 基本配置，只在第一次生效
    logging.basicConfig(
        level=logging.DEBUG,
        style='%',  # 指定format格式字符串的风格，可取值为'%'、'{'和'$'，默认为'%'
        format="%(asctime)s %(name)s %(levelname)s %(message)s",
        datefmt='%Y-%m-%d  %H:%M:%S %a',
        stream=None,  # stream和filename不能同时提供
        filename=None,
        filemode='a',
        handlers=None  # 一个创建了多个Handler的可迭代对象，这些handler将会被添加到root logger
    )


def _logger(ft, handler):
    # 日志器
    logger = logging.getLogger("root")
    logger.setLevel(logging.DEBUG)

    logger.addFilter(ft)
    logger.removeFilter(ft)

    logger.addHandler(handler)
    logger.removeHandler(handler)


def _handler(ft, formatter):
    # 处理器
    fh = logging.FileHandler("test.log", encoding="utf-8")
    ch = logging.StreamHandler()
    logging.NullHandler()

    # 将日志消息发送到磁盘文件，并支持日志文件按大小切割
    logging.handlers.RotatingFileHandler('logs/app.log', maxBytes=100, backupCount=5)
    # 将日志消息发送到磁盘文件，并支持日志文件按时间切割,backupCount保留3个旧log文件
    logging.handlers.TimedRotatingFileHandler("logs/app.log", when='S', interval=1, backupCount=3)

    fh.addFilter(ft)
    fh.removeFilter(ft)

    fh.setFormatter(formatter)
    fh.setLevel(logging.DEBUG)


def _formatter():
    # 格式器
    return logging.Formatter(
        style='%',
        fmt="%(asctime)s %(name)s %(filename)s %(message)s",
        datefmt="%Y/%m/%d %X"
    )


def _filter():
    # 过滤器
    class ContextFilter(logging.Filter):
        def filter(self, record):
            try:
                filter_key = record.TASK
            except AttributeError:
                return False

            if filter_key == "logToConsole":
                return True
            else:
                return False

    ContextFilter()


def _notice():
    # 基本消息提示，默认是root logger
    logging.debug("debug")
    logging.info("info")
    logging.warning("warning")
    logging.error("error")
    logging.critical("critical")


if __name__ == "__main__":
    # _help()
    pass
