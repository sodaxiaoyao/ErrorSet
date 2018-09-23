// 顶级公共函数
function say_hello() {
    console.log("hello,world")
}


// ===========builtin=============
// builtin---属性
console.log(Infinity);
console.log(NaN);
console.log(undefined);

// builtin---方法
decodeURI(encodeURI("my test.asp?name=ståle&car=saab"));
decodeURIComponent(encodeURIComponent("http://w3cschool.cc/my test.php?name=ståle&car=saab"));
eval("console.log('hello')");
isFinite(Infinity);
isNaN(2);
parseFloat('20.1');
parseInt('20.1');


// ===========Array=============
// Array---对象
let array_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let array_2 = new Array(3);
let array_3 = Array.from("01234567");

// Array---属性
Array.prototype.say_hello = say_hello;
array_1.say_hello();
array_1.constructor;
array_1.length;

// Array---方法
Array.isArray(array_1);
array_1.every(function (value) {
    return value > 0
});
array_1.some(function (value) {
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
// Boolean---对象
let trial_boolean = Boolean(1);

// Boolean---属性
Boolean.prototype.say_hello = say_hello;
trial_boolean.say_hello();
trial_boolean.constructor;

// Boolean---方法
trial_boolean.toString();
trial_boolean.valueOf();


// ===========Date=============
// Date---对象
let trial_date = new Date();

// Date---属性
Date.prototype.say_hello = say_hello;
trial_date.say_hello();
trial_date.constructor;

// Date---静态方法
Date();
Date.parse("2017/03/19");
Date.UTC(2005, 7, 8, 2, 3, 2, 1);

// Date---方法
trial_date.getDate();
trial_date.getDay();
trial_date.getMonth();
trial_date.getFullYear();
trial_date.getHours();
trial_date.getMinutes();
trial_date.getSeconds();
trial_date.getMilliseconds();
trial_date.setDate(15);
trial_date.setMonth(2);
trial_date.setFullYear(2012);
trial_date.setHours(2);
trial_date.setMinutes(2);
trial_date.setSeconds(2);
trial_date.setMilliseconds(2);
trial_date.setTime(2);
trial_date.getTime();
trial_date.getTimezoneOffset();
trial_date.getUTCDate();
trial_date.getUTCDay();
trial_date.getUTCMonth();
trial_date.getUTCFullYear();
trial_date.getUTCHours();
trial_date.getUTCMinutes();
trial_date.getUTCSeconds();
trial_date.getUTCMilliseconds();
trial_date.setUTCDate(2);
trial_date.setUTCMonth(2);
trial_date.setUTCFullYear(2018);
trial_date.setUTCHours(2);
trial_date.setUTCMinutes(2);
trial_date.setUTCSeconds(2);
trial_date.setUTCMilliseconds(2);
trial_date.toString();
trial_date.toDateString();
trial_date.toTimeString();
trial_date.toUTCString();
trial_date.toLocaleString();
trial_date.toLocaleTimeString();
trial_date.toLocaleDateString();
trial_date.valueOf();


// ===========Math=============
// Math---属性
Math.E;
Math.LN2;
Math.LN10;
Math.LOG2E;
Math.LOG10E;
Math.PI;
Math.SQRT1_2;
Math.SQRT2;

// Math---静态方法
Math.sin(Math.PI / 4);
Math.cos(Math.PI / 4);
Math.tan(Math.PI / 4);
Math.acos(20);
Math.asin(20);
Math.atan(20);
Math.atan2(0, 0);
Math.sqrt(4);
Math.pow(10, 2);
Math.exp(2);
Math.log(Math.E * Math.E);
Math.abs(-10);
Math.round(3.26);
Math.ceil(2.3);
Math.floor(2.8);
Math.max(10, 5);
Math.min(10, 5);
Math.random();
Math.valueOf();


// ===========Number=============
// Number---对象
let trial_num = Number('20');

// Number---属性
Number.prototype.say_hello = say_hello;
trial_num.say_hello();
trial_num.constructor;
Number.MAX_VALUE;
Number.MIN_VALUE;
Number.NaN;
Number.NEGATIVE_INFINITY;
Number.POSITIVE_INFINITY;

// Number---方法
trial_num.toString();
trial_num.toPrecision(2);
trial_num.toFixed(2);
trial_num.toExponential(2);
trial_num.valueOf();


// ===========String=============
// String---对象
let trial_str = String(5);

// String---属性
String.prototype.say_hello = say_hello;
trial_str.say_hello();
trial_str.constructor;
trial_str.length;

// String---方法
String.fromCharCode(72, 69, 76, 76, 79);
trial_str.anchor("name");
trial_str.link("http://www.w3school.com.cn/jsref/jsref_obj_string.asp");
trial_str.fixed();
trial_str.big();
trial_str.small();
trial_str.sub();
trial_str.sup();
trial_str.strike();
trial_str.italics();
trial_str.blink();
trial_str.bold();
trial_str.charAt(0);
trial_str.charCodeAt(1);
trial_str.concat("add");
trial_str.fontcolor("red");
trial_str.fontsize(7);
trial_str.indexOf("h");
trial_str.lastIndexOf("h");
trial_str.localeCompare("h");
trial_str.match("h");
trial_str.replace("a", "b");
trial_str.search('W3School');
trial_str.slice(1, 3);
trial_str.substr(3, 5);
trial_str.substring(3, 5);
trial_str.split(",");
trial_str.toLowerCase();
trial_str.toUpperCase();
trial_str.toLocaleLowerCase();
trial_str.toLocaleUpperCase();
trial_str.toString();
trial_str.valueOf();


// ===========RegExp=============
// RegExp---对象
let re = new RegExp("man", "gi");

// RegExp---属性
re.global;
re.multiline;
re.ignoreCase;
re.lastIndex;
re.source;

// RegExp---方法
re.compile();
re.exec("MAN");
re.test("MAN");


// ===========Window=============
// Window---静态属性
window.document;
window.navigator;
window.screen;
window.history;
window.location;
window.frames;
window.top;
window.self;
window.parent;
window.name;
window.length;
window.status;
window.defaultStatus;
window.devicePixelRatio;
window.closed;
window.innerHeight;
window.innerWidth;
window.outerHeight;
window.outerWidth;
window.pageXOffset;
window.pageYOffset;
window.screenLeft;
window.screenTop;
window.screenX;
window.screenY;

// Window---静态方法
window.alert("a");
window.confirm("Press a button!");
window.prompt("请输入您的名字", "Bill Gates");
window.requestAnimationFrame(null);
// 下列为了兼容IDE，实际应用把两个变量定义去掉
cancelIdleCallback = undefined;
requestIdleCallback = undefined;
//===========上面是多余部分===============
window.cancelIdleCallback(window.requestIdleCallback(function (deadline) {
    console.log("hello", deadline)
}));
window.clearInterval(window.setInterval(function () {
}, 1000));
window.clearTimeout(window.setTimeout(function () {
}, 1000));
window.print();
window.scrollBy(100, 100);
window.scrollTo(100, 100);
window.close();


// ===========Window-open=============
// Window-open---对象
let new_window = window.open('', 'new_window', 'width=200,height=100');

// Window-open---属性
new_window.opener;

// Window-open---方法
new_window.postMessage("hello", "*");
new_window.focus();
new_window.blur();
new_window.moveBy(50, 50);
new_window.moveTo(50, 50);
new_window.resizeBy(500, 300);
new_window.resizeTo(500, 300);


// ===========Navigator=============
// Navigator---静态属性
navigator.plugins;
navigator.appCodeName;
navigator.appName;
navigator.appVersion;
navigator.cookieEnabled;
navigator.onLine;
navigator.platform;
navigator.userAgent;

// Navigator---静态方法
navigator.javaEnabled();


// ===========Screen=============
// Navigator---静态属性
screen.height;
screen.width;
screen.availHeight;
screen.availWidth;
screen.colorDepth;
screen.pixelDepth;


// ===========History=============
// History---静态属性
history.length;

// History---静态方法
history.back();
history.forward();
history.go(-1);


// ===========Location=============
// Location---静态属性
location.hash;
location.host;
location.hostname;
location.href;
location.pathname;
location.port;
location.protocol;
location.search;

// Location---静态方法
location.assign("http://www.zyp233.cn");
location.reload();
location.replace("http://www.zyp233.cn");


// ===========Document=============
// Location---静态属性
document.all;
document.documentElement;
document.anchors;
document.applets;
document.forms;
document.images;
document.links;
document.body;
document.cookie;
document.domain;
document.lastModified;
document.referrer;
document.title;
document.URL;

// Document---静态方法
let newDoc = document.open("text/html", "replace");
newDoc.write("233");
newDoc.writeln("233");
newDoc.close();
document.getSelection();
document.getElementById("zyp");
document.getElementsByTagName("a");
document.getElementsByClassName("zyp");
document.getElementsByName("zyp");
document.querySelector("#a");
document.querySelectorAll("#score");
let my_li = document.createElement("li");
document.createTextNode("zyp");
let att = document.createAttribute("href");
att.value = "http://www.zyp233.cn";


// ===========Element=============
// Element---对象
let ele = document.getElementById('zyp');

// Element---属性
document.documentElement.namespaceURI;
ele.id;
ele.lang;
ele.innerHTML;
ele.innerText;
ele.textContent;
ele.tagName;
ele.nodeName;
ele.nodeType;
ele.nodeValue;
ele.title;
ele.style;
ele.className;
ele.attributes;
ele.ownerDocument;
ele.parentNode;
ele.childNodes.length;
ele.previousSibling;
ele.nextSibling;
ele.tabIndex;
ele.firstChild;
ele.lastChild;
ele.clientWidth;
ele.clientHeight;
ele.offsetWidth;
ele.offsetHeight;
ele.scrollHeight;
ele.scrollWidth;
ele.scrollTop;
ele.scrollLeft;
ele.offsetTop;
ele.offsetLeft;
ele.offsetParent;
ele.accessKey;
ele.dir;
ele.contentEditable;
ele.isContentEditable;

// Element---方法
document.documentElement.isDefaultNamespace('http://www.w3.org/1999/xhtml');
ele.insertBefore(my_li, my_li);
ele.appendChild(my_li);

ele.normalize();
ele.cloneNode(true);
ele.compareDocumentPosition(ele);
ele.removeAttribute("href");
ele.removeAttributeNode(ele.getAttributeNode("target"));
ele.removeChild(my_li);
ele.replaceChild(my_li, my_li);
ele.getAttribute("href");
ele.hasAttribute("href");
ele.hasAttributes();
ele.hasChildNodes();
ele.setAttribute("href", "http://www.zyp233.cn");
ele.setAttributeNode(att);
ele.isEqualNode(ele);
ele.isSameNode(ele);
ele.toString();
ele.item(0);


// ===========Attributes=============
// Attributes---属性
att.name;
att.value;
att.specified;
ele.attributes.length;

// Attribute---方法
ele.attributes.getNamedItem("href");
ele.attributes.item(0);
ele.attributes.removeNamedItem("href");
ele.attributes.setNamedItem(document.createAttribute("class"));


// ===========Event=============
// Event---监听事件
let eve = document.createElement("a");
eve.addEventListener("click", say_hello, true);

eve.onabort = say_hello;
eve.onerror = say_hello;
eve.onload = say_hello;
eve.onfocus = say_hello;
eve.onblur = say_hello;
eve.onchange = say_hello;
eve.onclick = say_hello;
eve.ondblclick = say_hello;
eve.onmouseup = say_hello;
eve.onmousedown = say_hello;
eve.onmousemove = say_hello;
eve.onmouseover = say_hello;
eve.onmouseout = say_hello;
eve.onkeydown = say_hello;
eve.onkeypress = say_hello;
eve.onkeyup = say_hello;
eve.onsubmit = say_hello;
eve.onreset = say_hello;
eve.onselect = say_hello;
window.onresize = say_hello;
window.onunload = say_hello;

// Event---触发事件
my_li.click();


// ===========smart_func=============
// 解释：一些优秀的写法(one code)
let range = (start, end) => new Array(end - start).fill(start).map((el, i) => start + i);
console.log(range);
console.log([...Array(5).keys()]);
Array.prototype.push.apply([], []);
Array.prototype.slice.call(document.getElementsByTagName("p"), 0);
console.log([...document.getElementsByTagName("p")]);
console.log(Object.prototype.toString.call({}) === "[object Object]");
