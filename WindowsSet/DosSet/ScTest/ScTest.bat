@echo off

::配置服务
rem sc config 服务名 start= AUTO    (自动)
rem sc config 服务名 start= DEMAND  (手动)
rem sc config 服务名 start= DISABLED(禁用)

::开启服务
rem net start 服务名

::关闭服务
net stop 服务名

::删除服务
sc delete 服务名 

::查询服务
sc query 服务名 

pause