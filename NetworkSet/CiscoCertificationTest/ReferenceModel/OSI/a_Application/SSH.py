# coding=utf-8

BYTES = 0xFF


class SecureShell(object):

    def __init__(self):
        pass

    @staticmethod
    def get_port(protocol):
        return {"tcp": 22, "udp": None}.get(protocol, None)
