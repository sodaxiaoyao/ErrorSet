my_cmd = {
}

user = {
}

privilege = {
}

config = {
    "ip subnet-zero": "Allow the first and last sub_nets to be used",
}

config_if = {
    "ip proxy-arp": "Open proxy arp"
}

my_cmd.update(user)
my_cmd.update(privilege)
my_cmd.update(config)
my_cmd.update(config_if)
