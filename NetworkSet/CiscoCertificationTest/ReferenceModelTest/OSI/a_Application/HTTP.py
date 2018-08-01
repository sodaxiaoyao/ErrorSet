# coding=utf-8

BYTES = 0xFF


class HyperTextTransferProtocol:

    def __init__(self):
        pass

    @staticmethod
    def get_port(protocol):
        return {"tcp": 80, "udp": None}.get(protocol, None)
