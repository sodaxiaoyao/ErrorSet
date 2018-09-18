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
    "erase startup-config": "删除保存信息",
    "write": "保存交换机设置内容",
    "copy running-config startup-config": "保存交换机设置内容",
    "reload": "重启交换机",

    "configure terminal": "Enter global configuration mode"
}

config = {
    "enable password": "特权界面加密",
    "banner motd": "创建登陆界面标识语",
    "service password-encryption": "加密enable密码",
    "enable secret": "设置enable加密密码",
    "hostname": "改变pc名称",

    "line [name": "Entering the line",
    "int [name": "Enter port",
}

config_if = {
    "password": "设置端口密码",
    "login": "开放登录",
    "ip address": "设置ip地址",
    "no shutdown": "启动端口",
    "clock rata 64000": "设置时钟频率",
    "duplex full/half": "配置单工或双工",
    "speed": "配置端口速率",
    "switchport mode access switchport access vlan 1": "添加端口到vlan",
    "switchport mode trunk": "跨vlan通信端口",
    "switchport trunk native vlan 1": "设置本地vlan",
    "switchport trunk allowed vlan 2,3": "允许通过的vlan"

}

my_cmd.update(user)
my_cmd.update(privilege)
my_cmd.update(config)
my_cmd.update(config_if)
