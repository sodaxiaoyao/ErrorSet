mysql -h 127.0.0.1 -u root -p password
-- 连接数据库

create database 数据库名 default character set utf8 collate utf8_general_ci;
create database 数据库名 default character set gbk collate gbk_chinese_ci;
-- 创建数据库

show variables like "% character %";
-- 查看数据库编码

set character_set_client = utf8;
set character_set_server = utf8;
set character_set_connection = utf8;
set character_set_database = utf8;
set character_set_results = utf8;
set collation_connection = utf8_general_ci;
set collation_database = utf8_general_ci;
set collation_server = utf8_general_ci;
-- 设置数据库编码

drop database 数据库名;
-- 删除数据库

show databases;
-- 查询数据库

use 数据库名;
-- 选择数据库

mysqldump -u 用户名 -p -d --add-drop-table  数据库名>d:\数据库名.sql
-- d:不导出数据只导出结构 add-drop-table:在每个create语句之前增加一个[drop table]

source 数据库名.sql
-- 导入数据库
