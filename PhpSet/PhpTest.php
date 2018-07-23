<?php
/**
 * php测试集合
 * User: SystemLight
 * Date: 2018/7/3
 * Time: 22:49
 */


namespace php_set;


//++++++++++++++++++++自定义类++++++++++++++++++++
class someClass
{
    function someMethod()
    {
    }
}


//++++++++++++++++++++内置函数++++++++++++++++++++
//=============类型校验=============
var_dump("str");
gettype("trial");

$trial = "32.3";
settype($trial, "int");

echo empty(null);
echo isset($trial);
is_numeric("23");
is_bool(true);
is_int(0);
is_float(0.1);
is_string("str");
is_object(new someClass());
is_callable(array(new someClass(), 'someMethod'), false, $callable_name);
is_resource("For example mysql");
is_null(null);
is_scalar("standard");
is_array(array("a", "b", "c"));


//++++++++++++++++++++原始数据类型++++++++++++++++++++
//=============boolean=============
$_boolean = true;
echo $_boolean;

//=============integer=============
$_integer = 0x1A;
echo $_integer;

//=============float=============
$_float = 0.111111;
echo $_float;

//=============string=============
$str = <<<EOD
Example of string
spanning multiple lines
using heredoc syntax.
EOD;
echo $str;

//=============array=============
//=============object=============
//=============callable=============
//=============resource=============
//=============NULL=============