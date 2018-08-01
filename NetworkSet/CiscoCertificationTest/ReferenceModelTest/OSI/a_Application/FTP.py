# coding=utf-8

BYTES = 0xFF


class FileTransferProtocol:

    def __init__(self):
        pass

    @staticmethod
    def get_port(protocol):
        return {"tcp": [20, 21], "udp": None}.get(protocol, None)
