@echo off

:: 帮助命令
help ver

:: 通信检测
ping www.baidu.com
tracert www.baidu.com
ipconfig

:: 终止进程
taskkill /F /pid 222

:: 查看活动连接
netstat -an


pause
