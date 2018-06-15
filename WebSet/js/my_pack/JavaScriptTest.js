function say_hello() {
    console.log("hello,world")
}


// ===========Array=============
let array_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let array_2 = new Array(3);
let array_3 = Array.from("01234567");

Array.prototype.say_hello = say_hello;
array_1.constructor;
array_1.length;

Array.isArray(array_1);
array_1.every(function (value) {
    return value > 0
});
array_1.some(function () {
    return value < 3;
});
array_1.filter(function (value) {
    return value > 5;
});
array_1.find(function (value) {
    return value < 3;
});
array_1.findIndex(function (value) {
    return value < 3;
});
array_1.forEach(function (value) {
    console.log(value);
});
array_1.map(function (value) {
    return value + 1;
});
array_1.reduce(function (total, value) {
    return total + value;
});
array_1.reduceRight(function (total, value) {
    return total + value;
});
array_1.concat(array_2);
array_1.copyWithin(0, 10, 11);
array_1.entries();
array_2.fill('value');
array_3.includes("3");
array_3.indexOf("3");
array_3.lastIndexOf("3");
array_3.join(",");
array_3.keys();
array_1.sort();
array_1.reverse();
array_1.slice(1, 3);
array_1.unshift("a");
array_1.push("c");
array_1.pop();
array_1.shift();
array_1.splice(0, 1);
array_1.toString();
array_1.toLocaleString();
array_1.valueOf();


// ===========Boolean=============
let trial_boolean = Boolean(1);

Boolean.prototype.say_hello = say_hello;
trial_boolean.constructor;

trial_boolean.toString();
trial_boolean.valueOf();


// ===========Date=============

