<?php
/**
 * php基本测试
 * User: SystemLight
 * Date: 2018/7/3
 * Time: 22:49
 */

namespace pt;

//===============array===============

//创建数组
$cars = array("Volvo", "BMW", "Toyota", "value");
echo "I like " . $cars[0] . ", " . $cars[1] . " and " . $cars[2] . "." . PHP_EOL;

$age = array("Bill" => "60", "Steve" => "56", "Mark" => "31");
echo $age["Bill"] . PHP_EOL;

//功能：切换数组键值大小写，可选的值CASE_LOWER | CASE_UPPER
array_change_key_case($age, CASE_UPPER);

//功能：数组分组
array_chunk($cars, 2);

$a = array(
    array(
        'id' => 5698,
        'first_name' => 'Bill',
        'last_name' => 'Gates',
    ),
    array(
        'id' => 4767,
        'first_name' => 'Steve',
        'last_name' => 'Jobs',
    ),
    array(
        'id' => 3809,
        'first_name' => 'Mark',
        'last_name' => 'Zuckerberg',
    )
);
//功能：返回数组中数组指定列
array_column($a, 'last_name','id');








