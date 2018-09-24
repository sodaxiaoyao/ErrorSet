create table table_name (
  type_1 int unsigned          not null auto_increment primary key,
  type_2 varchar(30)           not null default '默认数据',
  type_3 enum ('男', '女', '未知') not null,
  unique index index_name(type_2),
  foreign key (外键名) references 表名 (表属性)
    on delete cascade
);
-- 创建表格

DROP TABLE table_name;
-- 删除表格

delete
from table_name;
truncate table table_name;
-- 清空表格

RENAME TABLE
    table_name TO new_table_name;
-- 重命名表格

show tables;
-- 查看所有表格