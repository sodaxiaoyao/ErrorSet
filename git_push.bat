@echo off
echo "input the content of the commit��"
set /p commit_content=
echo %commit_content%
git add .
git commit -m %commit_content%
git push
pause