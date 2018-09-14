@echo off

:: view 查看资源
net view \\127.0.0.1

:: share 查看本地共享
net share
net share ipc$ \del

:: time 目标主机的时间
net time \\127.0.0.1 /set

:: use 建立远程链接
net use \\127.0.0.1\ipc$ "123" /user:"zyp"
net use h: \\127.0.0.1\myshare "123" /user:"zyp"
net use \\127.0.0.1\ipc$ /del

:: user 用户管理
net user zyp 123 /add
net user guest /active:yes
net user
net user zyp

:: localgroup 组管理
net localgroup Administrators zyp

:: start 服务管理
net start 
net pause
net stop

:: config 网络设置
net config


pause
