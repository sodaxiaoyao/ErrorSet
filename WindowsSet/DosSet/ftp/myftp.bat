@echo off


echo open 192.168.2.200>>ftp.tmp

echo kirito>>ftp.tmp

echo 111111>>ftp.tmp

echo put a.html>>ftp.tmp

echo bye>>ftp.tmp

ftp -i -s:ftp.tmp

del ftp.tmp


pause