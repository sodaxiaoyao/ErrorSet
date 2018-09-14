@echo off
echo "ÇëÊäÈëcommitµÄÄÚÈİ£º"
set /p commit_content=
echo %commit_content%
git add .
git commit -m %commit_content%
git push
pause