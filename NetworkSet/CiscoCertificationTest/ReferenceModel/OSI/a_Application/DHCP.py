# coding=utf-8

BYTES = 0xFF


class DynamicHostConfigurationProtocol(object):

    def __init__(self):
        pass

    @staticmethod
    def get_port(protocol):
        return {"tcp": None, "udp": 67}.get(protocol, None)
