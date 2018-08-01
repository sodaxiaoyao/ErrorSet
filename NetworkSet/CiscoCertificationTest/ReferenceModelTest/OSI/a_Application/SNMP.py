# coding=utf-8

BYTES = 0xFF


class SimpleNetworkManagementProtocol:

    def __init__(self):
        pass

    @staticmethod
    def get_port(protocol):
        return {"tcp": None, "udp": 161}.get(protocol, None)
