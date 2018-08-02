# coding=utf-8

BYTES = 0xFF


class EthernetII(object):

    def __init__(self):
        self.source = BYTES * 6
        self.destination = BYTES * 6

        self.type = BYTES * 2


def institute_of_electrical_and_electronics_engineers(numbering):
    class I3E802D3i(object):
        def __init__(self):
            self.alias_list = ["10Base-T"]

        def get_base_alias(self):
            print self.alias_list

        def print_base_alias(self, alias_num):
            alias_class = {
                "10Base-T": {
                    "speed": "10Mps",
                    "distance": "100m",
                    "medium": "3类非屏蔽双绞线(UTP)",
                    "connector": "Rj45"
                }
            }.get(self.alias_list[alias_num], None)

            for i in alias_class:
                print i + " : " + alias_class[i]

    class I3E802D3u(object):
        def __init__(self):
            self.alias_list = ["100Base-TX", "100Base-FX"]

        def get_base_alias(self):
            print self.alias_list

        def print_base_alias(self, alias_num):
            alias_class = {
                "100Base-TX": {
                    "speed": "100Mps",
                    "distance": "100m",
                    "medium": "5/5E/6类非屏蔽双绞线(UTP)",
                    "connector": "Rj45"
                },
                "100Base-FX": {
                    "speed": "100Mps",
                    "distance": "412m",
                    "medium": "62.5/125μm多模光纤",
                    "connector": "ST/SC"
                }
            }.get(self.alias_list[alias_num], None)

            for i in alias_class:
                print i + " : " + alias_class[i]

    class I3E802D3z(object):
        def __init__(self):
            self.alias_list = ["1000Base-CX", "1000Base-SX", "1000Base-LX"]

        def get_base_alias(self):
            print self.alias_list

        def print_base_alias(self, alias_num):
            alias_class = {
                "1000Base-CX": {
                    "speed": "1000Mps",
                    "distance": "25m",
                    "medium": "铜制双绞线",
                    "connector": "HS_SDC"
                },
                "1000Base-SX": {
                    "speed": "1000Mps",
                    "distance": "220/550m",
                    "medium": "850nm的激光62.5/50μm多模光纤",
                    "connector": "ST/SC"
                },
                "1000Base-LX": {
                    "speed": "1000Mps",
                    "distance": "10km",
                    "medium": "1300nm的激光9μm多模光纤",
                    "connector": "ST/SC"
                }
            }.get(self.alias_list[alias_num], None)

            for i in alias_class:
                print i + " : " + alias_class[i]

    class I3E802D3ab(object):
        def __init__(self):
            self.alias_list = ["1000Base-T"]

        def get_base_alias(self):
            print self.alias_list

        def print_base_alias(self, alias_num):
            alias_class = {
                "1000Base-T": {
                    "speed": "1000Mps",
                    "distance": "100m",
                    "medium": "5类非屏蔽双绞线(UTP)",
                    "connector": "Rj45"
                }
            }.get(self.alias_list[alias_num], None)

            for i in alias_class:
                print i + " : " + alias_class[i]

    class I3E802D3an(object):
        def __init__(self):
            self.alias_list = ["10GBase-T"]

        def get_base_alias(self):
            print self.alias_list

        def print_base_alias(self, alias_num):
            alias_class = {
                "10GBase-T": {
                    "speed": "10Gps",
                    "distance": "100m",
                    "medium": "5e/6/7类非屏蔽双绞线(UTP)",
                    "connector": "Rj45"
                }
            }.get(self.alias_list[alias_num], None)

            for i in alias_class:
                print i + " : " + alias_class[i]

    i3e_802_3 = {
        "802.3i": I3E802D3i(),
        "802.3u": I3E802D3u(),
        "802.3z": I3E802D3z(),
        "802.3ab": I3E802D3ab(),
        "802.3an": I3E802D3an(),
    }

    i3e = {}
    i3e.update(i3e_802_3)

    return i3e.get(numbering, None)
