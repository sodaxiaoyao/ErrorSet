# coding=utf-8

BYTES = 0xFF


class TransmissionControlProtocol:

    def __init__(self):
        self.source_port = BYTES * 2
        self.destination_port = BYTES * 2

        self.sequence_number = BYTES * 4
        self.acknowledgment_number = BYTES * 4

        self.window_size_value = BYTES * 2
        self.header_length = BYTES * 0.5
        self.flags = BYTES * 2

        self.urgent_pointer = BYTES * 2
        self.checksum = BYTES * 2

    @staticmethod
    def get_port():
        return 6
