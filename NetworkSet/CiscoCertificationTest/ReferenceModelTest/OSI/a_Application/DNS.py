# coding=utf-8

BYTES = 0xFF


class DomainNameSystem(object):

    def __init__(self):
        pass

    @staticmethod
    def get_port(protocol):
        return {"tcp": 53, "udp": 53}.get(protocol, None)
