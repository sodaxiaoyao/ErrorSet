@echo off
echo "������commit�����ݣ�"
set /p commit_content=
echo %commit_content%
git add .
git commit -m %commit_content%
git push
pause