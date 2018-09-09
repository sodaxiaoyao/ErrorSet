@echo off

::创建文件
mkdir %cd%\test\
md go..\

::改变位置
cd /d %~d0

::删除文件
rd /s /q %cd%\test\
rmdir /s /q %cd%\go..\

::输出内容，【>】重定向符号
echo "test" > test.txt

::显示文件内容
type test.txt

::循环语句 set(开始，步数，结尾)
for /l %%i in (1,1,6) do (echo %%i)

::显示当前目录
dir

::设置或者显示系统环境变量
path %PATH%;

::生成目录树
tree

::查看进程
tasklist


pause 