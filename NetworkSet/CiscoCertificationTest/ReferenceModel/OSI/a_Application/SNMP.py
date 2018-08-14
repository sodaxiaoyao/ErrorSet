# coding=utf-8

BYTES = 0xFF


class SimpleNetworkManagementProtocol(object):

    def __init__(self):
        pass

    @staticmethod
    def get_port(protocol):
        return {"tcp": None, "udp": 161}.get(protocol, None)

    def work_process(self):
        pass
