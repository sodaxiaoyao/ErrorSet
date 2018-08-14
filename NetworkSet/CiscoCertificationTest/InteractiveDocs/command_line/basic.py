my_cmd = {
    "exit": "Exit current mode"
}

user = {
    "enable": "Enter privileged mode"
}

privilege = {
    "configure terminal": "Enter global configuration mode"
}

config = {
    "line [name": "Entering the line",
    "int [name": "Enter port",
}

config_if = {
}

my_cmd.update(user)
my_cmd.update(privilege)
my_cmd.update(config)
my_cmd.update(config_if)
