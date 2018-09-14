@echo off

:: 查看计划任务列表
at

:: 添加计划任务
at 14:20 echo "hello" /yes /every:1

:: 删除计划任务
at 1 /del

:: 创建计划任务
schtasks /create /SC once /ST 20:02 /TN runname /TR c:\1.exe
schtasks /delete /TN runname

pause
