@echo off

:: 查看计划任务列表
at

:: 添加计划任务
at 14:20 echo "hello" /yes /every:1

:: 删除计划任务
at 1 /del


pause
