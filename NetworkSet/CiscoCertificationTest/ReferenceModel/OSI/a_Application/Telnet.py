# coding=utf-8

BYTES = 0xFF


class Telnet(object):

    def __init__(self):
        pass

    @staticmethod
    def get_port(protocol):
        return {"tcp": 23, "udp": None}.get(protocol, None)
