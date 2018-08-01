# coding=utf-8

BYTES = 0xFF


class InternetControlMessageProtocol:

    def __init__(self):
        self.type = BYTES * 1
        self.code = BYTES * 1

        self.checksum = BYTES * 2

    @staticmethod
    def get_port():
        return 1

    def get_type(self, num):
        if num < self.type:
            return {
                0: "回送请求或回答",
                3: "终点不可达",
                5: "改变路由",
                8: "回送请求或回答",
                11: "时间超过",
                12: "参数问题",
                13: "时间戳请求或回答",
                14: "时间戳请求或回答",
            }.get(num, None)
