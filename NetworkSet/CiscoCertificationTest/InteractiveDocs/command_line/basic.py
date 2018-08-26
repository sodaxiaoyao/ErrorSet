my_cmd = {
    "exit": "Exit current mode",
    "end": "Exit to privileged mode",
    "disable": "Exit to user mode",
    "logout": "Exit user mode",
    "no [name": "cancel configure"
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
