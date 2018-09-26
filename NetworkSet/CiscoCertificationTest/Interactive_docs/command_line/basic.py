my_cmd = {
    "copy": "复制命令",
    "exit": "退出当前模式",
    "end": "退出特权模式",
    "disable": "退出用户模式",
    "logout": "退出用户模式",
    "no": "取消配置",
}

user = {
    "enable": "进入特权模式"
}

privilege = {
    "erase startup-config": "删除保存信息",
    "write": "保存交换机设置内容",
    "copy running-config startup-config": "保存交换机设置内容",
    "reload": "重启交换机",
    "clock set": "设置时间",
    "terminal history": "历史记录操作",
    "debug ip routing": "开启路由Debug",
    "configure terminal": "进入全局配置模式"
}

config = {
    "enable password": "特权界面加密",
    "banner motd": "创建登陆界面标识语",
    "service password-encryption": "加密enable密码",
    "enable secret": "设置enable加密密码",
    "hostname": "改变pc名称",
    "ip host": "设置hosts文件",
    "no ip domain-lookup": "关闭域名查询",
    "clock rate": "(DCE)设置时钟频率",
    "ip default-gateway": "设置网关",
    "line": "进入线路",
    "int": "进入端口",
}

config_if = {
    "password": "设置端口密码",
    "login": "开放登录",
    "ip address": "设置ip地址",
    "no shutdown": "启动端口",
    "clock rata 64000": "设置时钟频率",
    "duplex full/half": "配置单工或双工",
    "speed": "配置端口速率",
    "description": "添加端口描述",
    "bandwidth": "设置端口带宽",
    "delay": "设置延时",
    "switchport mode access switchport access vlan 1": "添加端口到vlan",
    "switchport mode trunk": "跨vlan通信端口",
    "switchport trunk native vlan 1": "设置本地vlan",
    "switchport trunk allowed vlan 2,3": "允许通过的vlan"
}

my_cmd.update(user)
my_cmd.update(privilege)
my_cmd.update(config)
my_cmd.update(config_if)
