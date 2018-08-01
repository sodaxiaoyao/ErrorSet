# coding=utf-8

BYTES = 0xFF


class UserDatagramProtocol:

    def __init__(self):
        self.source_port = BYTES * 2
        self.destination_port = BYTES * 2

        self.length = BYTES * 2
        self.destination_port = BYTES * 2

    @staticmethod
    def get_port():
        return 17
