@echo off

:: 帮助命令
help ver

:: 控制台颜色
color /?

:: 通信检测
ping www.baidu.com
tracert www.baidu.com
ipconfig

:: 终止进程
taskkill /F /pid 222

:: 查看活动连接
netstat -an

:: 关机命令
shutdown -i -s -f -t 60 -c "关机"
shutdown -i -r -f -t 60 -c "重启"
shutdown -i -l -f -t 60 -c "注销"
shutdown -a


pause
