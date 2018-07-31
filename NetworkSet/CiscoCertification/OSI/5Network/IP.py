# coding=utf-8

BYTES = 0xFF


class InternetProtocol:

    def __init__(self):
        self.source = BYTES * 4
        self.destination = BYTES * 4

        self.version = BYTES * 0.5
        self.header_length = BYTES * 0.5
        self.differentiated_services_field = BYTES * 1
        self.total_length = BYTES * 2

        self.identification = BYTES * 2
        self.flags = BYTES * 0.375
        self.fragment_offset = BYTES * 1.625

        self.time_to_live = BYTES * 1
        self.protocol = BYTES * 1

        self.header_checksum = BYTES * 2
