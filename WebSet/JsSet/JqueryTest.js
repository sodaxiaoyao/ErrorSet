//===基于jQuery
let $ = jQuery;

/*
sj_connect:
    $.ajax()
    $.get()
    $.post()
    $.getJSON()
    $.getScript()
    $.ajaxSetup()
    $.ajaxSend()
    $.ajaxStart()
    $.ajaxError()
    $.ajaxSuccess()
    $.ajaxComplete()
    $.ajaxStop()

    $(form_dom).serialize()---------->序列化表单+拼接串
    $(form_dom).serializeArray()---------->序列化表单+数组
    $(dom).load(url)---------->嵌入远程html
*/

/*
sj_traverse:
    $(dom).each(func)---------->遍历所有匹配的dom元素
    $(dom).map(func)---------->遍历dom列表，返回数组
    $(dom).queue(func)---------->dom元素的动画个数,可以添加新的队列
    $(dom).dequeue()---------->从队列最前端移除一个队列函数，并执行他。
    $(dom).clearQueue()---------->清空对象上尚未执行的所有队列
    $(dom).length---------->存在匹配的dom的数量
*/

/*
sj_find:
    $(dom).is(dom)---------->判断是否是该类dom
    $(dom).has(dom)---------->含有特定的dom
    $(dom).not(dom)---------->匹配没有某些dom的集合

    $(dom).index(dom)---------->查找dom的位置
    $(dom).get(int)---------->选取dom列表的某个dom,返回array
    $(dom).eq(int)---------->选取dom列表的某个dom
    $(dom).filter(content)---------->过滤dom列表
    $(dom).closest(dom)---------->从当前元素不断向上查找
    $(dom).slice(int,int)---------->数据集合切片
    $(dom).find(dom)---------->查找dom中的

    $(dom).parent()---------->获取父元素
    $(dom).parents()---------->获取父元素集合
    $(dom).parentsUntil(dom)---------->查找当前元素的所有的父辈元素，直到遇到匹配的那个元素为止
    $(dom).offsetParent()---------->获取第一个被定位的父元素
    $(dom).siblings()---------->查找同辈元素
    $(dom).children()---------->获取子元素

    $(dom).end---------->获取最近的一次破坏性操作之前
    $(dom).prev()---------->获取当前元素紧挨着的元素--前面
    $(dom).prevAll()---------->获取当前元素紧挨着的所有元素--前面
    $(dom).prevUntil(dom)---------->获取当前元素紧挨着的所有元素，直到某个dom截止--前面
    $(dom).next()---------->获取当前元素紧挨着的元素
    $(dom).nextAll()---------->获取当前元素紧挨着的所有元素
    $(dom).nextUntil(dom)---------->获取当前元素紧挨着的所有元素，直到某个dom截止
*/

/*
sj_dom:
    $.cssHooks.name = {get: function( elem, computed, extra ) {},set: function( elem, value ) {}}
    $(dom).offset()---------->获取或设置当前视口的相对偏移
    $(dom).position()---------->获取或设置相对父元素的偏移
    $(dom).scrollTop()---------->获取或设置滚动条的上偏移
    $(dom).scrollLeft()---------->获取或设置滚动条的左偏移
    $(dom).height()---------->获取或设置高度
    $(dom).width()---------->获取或设置宽度
    $(dom).innerHeight()---------->获取或设置内高度
    $(dom).innerWidth()---------->获取或设置内宽度
    $(dom).outerHeight()---------->获取或设置外高度
    $(dom).outerWidth()---------->获取或设置外宽度

    $(dom).attr()---------->获取或设置dom的属性
    $(dom).removeAttr(attr)---------->移除dom上的属性
    $(dom).prop()---------->标准化获取或设置dom的属性
    $(dom).removeProp(attr)---------->标准化移除dom上的属性

    $(dom).addClass(class)---------->添加class
    $(dom).removeClass(class)---------->删除class
    $(dom).toggleClass(class)---------->切换class
    $(dom).hasClass(class)---------->判断是否有class

    $(dom).html()---------->获取或设置html
    $(dom).text()---------->获取或设置text
    $(dom).contents()---------->获取文本和结点的集合
    $(dom).val()---------->获取或设置value
    $(dom).css()---------->获取或设置style

    $(dom).addBack(dom)---------->把之前的元素也加入到匹配中
    $(dom).add(dom)---------->添加dom到jquery集合中
    $(dom).append(html)---------->添加html
    $(dom).appendTo(dom)----------用于被追加的内容
    $(dom).prepend(html)---------->前面添加html
    $(dom).prependTo(dom)---------->前面用于被追加的内容
    $(dom).after(dom)---------->段落后面添加
    $(dom).before(dom)---------->段落前面添加
    $(dom).insertAfter(dom)---------->将dom插入到之后
    $(dom).insertBefore(dom)---------->将dom插入到之前
    $(dom).wrap(dom)---------->令某个dom成为自己的包裹元素
    $(dom).unwrap(dom)---------->移除父元素的包裹
    $(dom).wrapAll(dom)---------->令所有匹配元素被dom包裹
    $(dom).wrapInner(dom)---------->反向包裹
    $(dom).replaceWith(dom)---------->替换掉dom
    $(dom).replaceAll(dom)---------->替换掉所有dom
    $(dom).empty()---------->清空dom内部内容
    $(dom).remove()---------->移除被选中dom
    $(dom).detach()---------->移除被选中dom,保留事件
    $(dom).clone(boolean)---------->克隆dom，true值的话连同事件一起clone
*/

/*
sj_event:
    $(window).resize()---------->屏幕大小事件改变
    $(dom).on(event,func)---------->添加事件
    $(dom).off(event)---------->移除事件
    $(dom).one(event,func)---------->执行一次的事件
    $(dom).trigger(event)---------->触发事件
    $(dom).triggerHandler(event)---------->优化了trigger

    $(dom).toggle()---------->元素可见状态
    $(dom).hide()---------->元素隐藏
    $(dom).show()---------->元素显示
    $(dom).slideToggle()---------->滑动
    $(dom).slideUp()---------->滑动
    $(dom).slideDown()---------->滑动
    $(dom).fadeToggle()---------->淡变
    $(dom).fadeIn()---------->淡变
    $(dom).fadeOut()---------->淡变
    $(dom).fadeTo("slow", .3)---------->淡变
    $.fx.off = true---------->关闭所有动画
    $(dom).animate(styles,{"step":"","callback":""})---------->动画
    $(dom).finish()---------->立即完成动画
    $(dom).delay(int)---------->延时
    $(dom).stop(int)---------->停止动画

    $(dom).blur()---------->失去焦点
    $(dom).change()---------->内容改变事件
    $(dom).click()---------->点击事件
    $(dom).dblclick()---------->双击事件
    $(dom).focus()---------->获取焦点
    $(dom).focusin()---------->选中事件
    $(dom).focusout()---------->选出事件
    $(dom).scroll()---------->dom滚动事件
    $(dom).select()---------->dom被选中事件
    $(dom).submit()---------->dom提交事件

    $(dom).keypress()---------->键盘和按钮按下事件
    $(dom).keydown()---------->键盘按下事件
    $(dom).keyup()---------->键盘抬起事件

    $(dom).mousedown()---------->鼠标按下事件
    $(dom).mouseenter()---------->鼠标指针穿过元素
    $(dom).mouseleave()---------->鼠标指针离开元素
    $(dom).mousemove()---------->鼠标移动事件
    $(dom).mouseout()---------->鼠标移动开元素
    $(dom).mouseup()---------->鼠标抬起的时候
    $(dom).mouseover()---------->鼠标在元素上面
    $(dom).hover(over,out)---------->鼠标事件
*/

/*
sj_storage:
    $(dom).data(key,value)---------->存储和获取dom上的数据
    $(dom).removeData(key)---------->删除dom上的数据
*/

/*
sj_tool:
    $.each(set,func)---------->遍历数据
    $.extend(obj1,obj2)---------->合并两个对象
    $.grep(set,func)---------->过滤集合
    $.Deferred()
    $.makeArray()---------->转换类数组为真数组
    $.map()---------->map
    $.inArray()---------->索引元素位置
    $.toArray()---------->转换数组
    $.merge()---------->合并两个数组
    $.uniqueSort()---------->删除重复dom
    $.parseXML(string)---------->解析为xml
    $.parseHTML()---------->解析为html
    $.parseJSON()---------->解析为json
    $.noop()---------->空函数
    $.proxy()---------->代理执行类的方法
    $.contains()---------->dom中是否包含dom
    $.type()---------->检测类型
    $.isEmptyObject({})---------->检测对象是否为空
    $.isPlainObject({})---------->检测是否为纯粹的对象
    $.isNumeric()---------->检测是否为数字
    $.isWindow(window)---------->检测是否为窗口
    $.trim()---------->去除空格
    $.param()---------->序列化object
    $.error()---------->错误信息
    $.now()---------->返回时间戳
    $.fn.jquery---------->jquery版本号
*/


//===核心代码
let _s = (function () {

    //核心
    let sj = function (args) {
        return new sj.fn.init(args);
    };

    //原型
    sj.fn = sj.prototype = {
        constructor: sj,
        init: function (dom_obj) {
            if (dom_obj) {

            }
        }
    };

    //拓展
    sj.extends = function (methods) {
        if (sj.is_obj(methods)) {
            $.extend(sj, methods);
            return true
        }
        return false
    };

    //内置库
    sj.is_obj = function (obj) {
        return Object.prototype.toString.call(obj) === "[object Object]";
    };
    sj.extends({
        "debug": false,
        "_debug_fun": function (str) {
            if (this.debug) {
                console.log(str);
            }
        },
    });

    //模块
    sj.module = {
        "module_pool": {
            "sj_connect": sj_connect,
        },
        "load": function (module) {
            try {
                this.module_pool[module]();
                return true
            } catch (e) {
                sj._debug_fun(e);
                sj._debug_fun("加载的模块名称可能不正确");
                return false
            }
        },
        "loads": function (m_list) {
            let tmp;
            for (tmp of m_list) {
                this.load(tmp);
            }
        },
        "del": function (module) {
            try {
                delete this.module_pool[module];
                return true
            } catch (e) {
                sj._debug_fun(e);
                sj._debug_fun("删除的名称可能不正确");
                return false
            }
        },
        "put": function (name, module) {
            this.module_pool[name] = module;
        },
        "puts": function (modules) {
            if (sj.is_obj(modules)) {
                $.extend(this.module_pool, modules);
                return true
            }
            return false
        },
    };

    //校正
    sj.fn.init.prototype = sj.fn;

    //提交
    return sj;

})();

function sj_connect() {
    //connect库
    _s.extends({
        "jsp_arg": "json_callback",

        "jsp": function (url, callback, data) {
            let that = this;
            this._debug_fun("发送的数据");
            this._debug_fun(data);
            return $.getJSON(`${url}?${that.jsp_arg}=?`, data, function (result) {
                if (callback) {
                    that._debug_fun("jsp返回的数据");
                    that._debug_fun(result);
                    callback(result)
                } else {
                    console.log("请求数据", result)
                }
            });
        },
        "req": function (url, callback, data, type, kind) {
            let that = this;
            return $.ajax({
                url: url,
                data: data || {},
                async: true,
                cache: true,
                global: true,
                crossDomain: false,
                processData: true,
                context: null,
                type: ["GET", "POST", "PUT", "DELETE"][type || 0],
                contentType: ["application/x-www-form-urlencoded", "application/json"][kind || 0],
                converters: {
                    "* text": window.String,
                    "text html": true,
                    "text json": $.parseJSON,
                    "text xml": $.parseXML
                },
                statusCode: {
                    404: function () {
                        that._debug_fun("页面未找到");
                    },
                    500: function () {
                        that._debug_fun("服务器错误");
                    }
                },
                dataFilter: function (data, type) {
                    console.log(type);
                    return data
                },
                beforeSend: function (xhr) {
                    console.log(xhr);
                    that._debug_fun("请求开始");
                    return true;
                },
                error: function () {
                    that._debug_fun("请求错误");
                },
                success: function (data, text_status, jq_xhr) {
                    console.log(text_status, jq_xhr);
                    let _self = $(this);
                    if (callback) {
                        callback(data, _self)
                    } else {
                        console.log("返回数据", data);
                    }
                },
                complete: function (xhr, ts) {
                    console.log(xhr, ts);
                    that._debug_fun("请求完成");
                }
            });
        },
        "get": function (url, callback, data, kind) {
            let kind_pool = kind ? ["_default", "html", "xml", "script", "text"][kind] : undefined;
            return $.get(url, data, function (result) {
                if (callback) {
                    callback(result);
                } else {
                    console.log("get请求数据", result);
                }
            }, kind_pool);
        },
        "post": function (url, callback, data, kind) {
            let kind_pool = kind ? ["_default", "html", "xml", "script", "text"][kind] : undefined;
            return $.post(url, data, function (result) {
                if (callback) {
                    callback(result);
                } else {
                    console.log("post请求数据", result);
                }
            }, kind_pool);
        },
    });
}

_s.module.loads([
    "sj_connect",
    "sj_datetime",
]);


//Deferred对象使用案例
let wait = function (callback) {
    let dtd = $.Deferred();
    callback(function () {
        console.log("释放");
        dtd.resolve();
    });
    return dtd.promise();
};
$.when(wait(function (res) {
    console.log("事件");
    setTimeout(res, 2000);
})).done(function () {
    console.log("哈哈，成功了！");
}).fail(function () {
    console.log("出错啦！");
}).then(
    //相当于done和fail集合
    function () {
        alert("成功");
    },
    function () {
        alert("失败");
    }
);
