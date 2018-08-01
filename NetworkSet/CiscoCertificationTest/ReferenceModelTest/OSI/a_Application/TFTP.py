# coding=utf-8

BYTES = 0xFF


class TrivialFileTransferProtocol:

    def __init__(self):
        pass

    @staticmethod
    def get_port(protocol):
        return {"tcp": None, "udp": 69}.get(protocol, None)
