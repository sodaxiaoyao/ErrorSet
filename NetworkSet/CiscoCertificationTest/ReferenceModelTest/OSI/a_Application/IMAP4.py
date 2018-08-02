# coding=utf-8

BYTES = 0xFF


class InternetMessageAccessProtocol4(object):

    def __init__(self):
        pass

    @staticmethod
    def get_port(protocol):
        return {"tcp": 143, "udp": None}.get(protocol, None)
