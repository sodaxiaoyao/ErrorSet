# coding=utf-8

BYTES = 0xFF


class SimpleMailTransferProtocol(object):

    def __init__(self):
        pass

    @staticmethod
    def get_port(protocol):
        return {"tcp": 25, "udp": None}.get(protocol, None)
