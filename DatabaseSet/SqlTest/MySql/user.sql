CREATE USER 'username'@'%' IDENTIFIED BY 'password';
-- 创建用户

DROP USER 'username'@'host';
-- 删除用户

GRANT ALL ON *.* TO 'username'@'%';
-- 分配权限
REVOKE all ON databasename.tablename FROM 'username'@'host';
-- 撤销权限
show grants for 'username'@'%';
-- 查询权限

SET PASSWORD FOR 'username'@'host' = PASSWORD('newpassword');
-- 设置密码

UPDATE USER set authentication_string=PASSWORD("111111") WHERE user='zyp';
flush privileges;
-- 修改内容

SELECT DISTINCT CONCAT('User: ''',user,'''@''',host,''';') AS query FROM mysql.user;
-- 查询用户
