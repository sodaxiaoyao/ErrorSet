my_cmd = {
}

user = {
}

privilege = {
}

config = {
    "ip subnet-zero": "允许使用0和1做为子网",
}

config_if = {
    "ip proxy-arp": "开启ARP代理"
}

my_cmd.update(user)
my_cmd.update(privilege)
my_cmd.update(config)
my_cmd.update(config_if)
