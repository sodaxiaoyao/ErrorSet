@echo off

:: 打开文件
start d:\1.txt 

:: 复制文件
copy d:\1.txt c:\

:: 目录下的所有文件
xcopy /E e:\test e:\

:: 重命名文件
ren e:\3.txt test.txt

:: 比较文件的差异性
fc e:\1.txt e:\2.txt

:: 设置文件属性
attrib /S /D +H +R e:\test

:: 删除文件
del e:\test

:: 清楚屏幕
cls

:: 查看dos版本号
ver

:: 显示或者设置日期
date

:: 显示或者设置时间
time


pause
