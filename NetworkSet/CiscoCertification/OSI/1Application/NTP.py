# coding=utf-8

BYTES = 0xFF


class NetworkTimeProtocol:

    def __init__(self):
        pass

    @staticmethod
    def get_port(protocol):
        return {"tcp": None, "udp": 123}.get(protocol, None)