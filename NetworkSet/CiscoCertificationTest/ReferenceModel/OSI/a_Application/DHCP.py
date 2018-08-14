# coding=utf-8

BYTES = 0xFF


class DynamicHostConfigurationProtocol(object):

    def __init__(self):
        pass

    @staticmethod
    def get_port(protocol):
        return {"tcp": None, "udp": 67}.get(protocol, None)

    def post_discover(self):
        pass

    def get_offer(self):
        pass

    def post_request(self):
        pass

    def get_ack(self):
        pass

    def work_process(self):
        self.post_discover()
        self.get_offer()
        self.post_request()
        self.get_ack()
