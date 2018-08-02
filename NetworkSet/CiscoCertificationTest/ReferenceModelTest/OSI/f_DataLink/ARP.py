# coding=utf-8

BYTES = 0xFF


class AddressResolutionProtocol(object):

    def __init__(self):
        self.hardware_type = BYTES * 2
        self.protocol_type = BYTES * 2
        self.hardware_size = BYTES * 1
        self.protocol_size = BYTES * 1

        self.sender_mac_address = BYTES * 6
        self.sender_ip_address = BYTES * 4
        self.target_mac_address = BYTES * 6
        self.target_ip_address = BYTES * 4

        self.option_code = BYTES * 2
