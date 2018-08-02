# coding=utf-8

BYTES = 0xFF


class PostOfficeProtocolVersion3(object):

    def __init__(self):
        pass

    @staticmethod
    def get_port(protocol):
        return {"tcp": 110, "udp": None}.get(protocol, None)
