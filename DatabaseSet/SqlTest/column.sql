INSERT INTO data_base_name () VALUES();
-- 插入一行数据

delete from data_base_name where type_1 = '1';
-- 删除一行数据

alter table data_base_name add address varchar(10) null;
-- 1.添加新列
alter table data_base_name change address address int not null;
-- 2.修改列
alter table data_base_name drop column address;
-- 3.删除列
show columns from data_base_name;
-- 查询所有列

select * from data_base_name;
-- 查询所有数据
