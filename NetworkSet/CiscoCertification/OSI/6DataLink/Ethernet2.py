# coding=utf-8

BYTES = 0xFF


class EthernetII:

    def __init__(self):
        self.source = BYTES * 6
        self.destination = BYTES * 6

        self.type = BYTES * 2
