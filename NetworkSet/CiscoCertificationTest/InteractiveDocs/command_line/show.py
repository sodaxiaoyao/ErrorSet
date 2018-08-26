my_cmd = {
}

user = {
}

privilege = {
    "show running-config": "Show configuration information",
    "show history": "View history",
    "show terminal": "View history buffer size",
}

config = {
}

config_if = {
}

my_cmd.update(user)
my_cmd.update(privilege)
my_cmd.update(config)
my_cmd.update(config_if)
