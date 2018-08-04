# coding=utf-8

"""
实现功能：
    1.获取网络地址
    2.获取广播地址
    3.根据主机数量计算子网掩码/掩码位
    4.根据子网掩码获取主机数量
    5.子网掩码转换为掩码位
    6.掩码位转换为子网掩码
    7.根据数量大小查询到最接近的位数
    8.子网打印功能
"""


class IPDetails(object):

    def __init__(self, ip, sub_mask=None):
        classless = ip.split("/")
        self.ip_list = self.get_ip_list(classless[0])
        if sub_mask is None:
            self.mask = abs(int(classless[1])) if len(classless) == 2 else self.__get_mask()
            assert 0 <= self.mask <= 32, "错误的掩码"
        else:
            self.mask = self.conversion_mask(sub_mask)
        self.__div_mod = [self.mask / 8, self.mask % 8]
        self.source_website = self.website_address
        self.source_mask = self.mask

    def __get_mask(self):
        # 功能：获取传入IP的默认位数
        class_range = int(self.ip_list[0])
        if 0 <= class_range <= 127:
            return 8
        elif 128 <= class_range <= 191:
            return 16
        elif 192 <= class_range <= 223:
            return 24
        else:
            raise TypeError("错误的地址")

    def __get_address(self, this_type):
        # 功能：获取广播地址/网络地址
        opt_type = {
            0: ["0", "0"],
            1: ["1", "255"]
        }.get(this_type, None)
        address_list = []
        local_i = 0
        for local_i in range(self.__div_mod[0]):
            address_list.append(self.ip_list[local_i])
        local_i += 1
        if self.__div_mod[1] > 0:
            ip_bin = bin(int(self.ip_list[local_i])).replace("0b", "").zfill(8)
            address_list.append(str(int(ip_bin[0:self.__div_mod[1]].ljust(8, opt_type[0]), 2)))
        address_list.extend([opt_type[1]] * (4 - len(address_list)))
        return ".".join(address_list) + "\n"

    def conversion_mask(self, sub_mask):
        # 功能：将子网掩码转换成掩码位
        ip_list = self.get_ip_list(sub_mask)
        tmp_mask = 0
        for i in ip_list:
            if i == "255":
                tmp_mask += 8
            else:
                ip_bin = bin(int(i)).replace("0b", "").zfill(8)
                for j in ip_bin:
                    if j == "1":
                        tmp_mask += 1
                    else:
                        break
                break
        return tmp_mask

    def max_pc_size(self, sub_mask, re=False):
        # 功能：获取最大主机数/子网掩码
        if re:
            bit_size = 32 - self.find_bit(sub_mask)
            return [self.re_conversion_mask(bit_size).strip('\n'), bit_size]
        else:
            return 2 ** (32 - self.conversion_mask(sub_mask)) - 2

    def set_subnet(self, subnet_size, is_zero=True):
        # 功能：设置子网划分位
        bit_size = self.find_bit(subnet_size, is_zero)
        bit_size += self.mask
        if bit_size > 30:
            print "主机位不足，请重新设置"
        else:
            self.mask = bit_size
            self.__div_mod = [self.mask / 8, self.mask % 8]

    def clear_subnet(self):
        # 功能：清除子网划分
        self.mask = self.source_mask
        self.__div_mod = [self.mask / 8, self.mask % 8]

    def print_all_subnet(self):
        # 功能：打印子网，进行划分
        print "=============承载主机数：" + str(2 ** (32 - self.mask) - 2) + "==============="
        sub_size = self.mask - self.source_mask
        if sub_size <= 0:
            print "未进行子网段设置"
        else:
            offset_min = sub_size / 8
            offset_max = offset_min + int(sub_size % 8 != 0)
            ip_list = self.get_ip_list(self.website_address.strip("\n"))
            source_site = self.source_mask % 8
            ip_id = self.__div_mod[0] - offset_min
            ip_mod = bin(int(ip_list[ip_id])).replace("0b", "").zfill(8)[0:self.__div_mod[1]]
            source_ip = ip_mod[0:source_site]
            for i in range(2 ** sub_size):
                the_ip_net = bin(i).replace("0b", "").zfill(sub_size)
                tmp = (source_ip + the_ip_net).ljust(8 * offset_max, '0')
                for k in range(offset_max):
                    begin = k * 8
                    ip_list[ip_id + k] = str(int(tmp[begin:begin + 8], 2))
                print ".".join(ip_list) + "/" + str(self.mask)
        print "========================================="

    @property
    def website_address(self):
        # 功能：网络地址
        return self.__get_address(0)

    @property
    def broadcast_address(self):
        # 功能：广播地址
        return self.__get_address(1)

    @staticmethod
    def get_ip_list(ip_address):
        # 功能：获取掩码列表
        ip_list = ip_address.split(".")
        for the_ip in ip_list:
            assert 0 <= int(the_ip) < 256, "错误的地址"
        return ip_list

    @staticmethod
    def find_bit(sub_size, is_zero=False):
        # 功能：根据大小查询需要的二进制位数
        zero = 2 if is_zero else 0
        bit_size = 0
        tmp_pc_size = 0
        while True:
            tmp_pc_size += 2 ** bit_size
            bit_size += 1
            if (tmp_pc_size + zero) > sub_size:
                return bit_size

    @staticmethod
    def re_conversion_mask(mask_size):
        # 功能：将掩码位转换成子网掩码
        assert 0 <= mask_size <= 32, "超出正常范围"
        tmp_mask = []
        div_mod = [mask_size / 8, mask_size % 8]
        tmp_mask.extend(["255"] * div_mod[0])
        if div_mod[1] > 0:
            tmp_mask.append(str(int(("1" * div_mod[1]).ljust(8, "0"), 2)))
        tmp_mask.extend(["0"] * (4 - len(tmp_mask)))
        return ".".join(tmp_mask) + "\n"
