@echo off

:: 格式化磁盘
rem format e: /Q /FS:ntfs /v:卷标

:: 查看磁盘状态
chkdsk e: 

:: 重命名卷标
rem label e: Cloud

:: 显示卷标
vol e:


pause
