let page = getCurrentPages();
let app = getApp();
let util = require("../UtilsTest/UtilsTest.js");
Page({
  data: {

    latitude: 23.099994,
    longitude: 113.324520,
    markers: [{
      id: 1,
      latitude: 23.099994,
      longitude: 113.324520,
      title: 'T.I.T 创意园',
      iconPath: "",
      rotate: 0,
      alpha: 1,
      width: 20,
      height: 20,
      callout: {
        content: "文本",
        color: "blue",
        fontSize: 30,
        borderRadius: 10,
        bgColor: "yellow",
        padding: 5,
        display: "BYCLICK",
        textAlign: "center"
      },
      label: {
        content: "label文本",
        color: "blue",
        fontSize: 30,
        anchorX: 23.099998,
        anchorY: 113.324520,
        borderWidth: 5,
        borderColor: "red",
        borderRadius: 15,
        bgColor: "green",
        padding: "18",
        textAlign: "center",
      },
      anchor: {
        x: 0.5,
        y: 1
      }
    }],
    polyline: [{
      points: [{
        longitude: 23,
        latitude: 23
      }, {
        longitude: 23.1,
        latitude: 23.1
      }],
      color: "#FF0000DD",
      width: 20,
      dottedLine: true,
      arrowLine: true,
      arrowIconPath: undefined,
      borderColor: "#fff",
      borderWidth: 8
    }],
    circles: [{
      latitude: 23.099994,
      longitude: 113.324520,
      color: '#FF0000DD',
      fillColor: '#7cb5ec88',
      radius: 3000,
      strokeWidth: 1
    }],
    controls: [{
        id: 1,
        iconPath: '../images/ImageTest.jpg',
        position: {
          left: 180,
          top: 100 - 50,
          width: 20,
          height: 20
        },
        clickable: true
      },
      {
        id: 2,
        iconPath: '../images/ImageTest.jpg',
        position: {
          left: 200,
          top: 100 - 50,
          width: 20,
          height: 20
        },
        clickable: true
      }
    ],



    data_test: "data_test_data",
    data_test_array: [...Array(5).keys()],
    nodes: [{
      name: 'a',
      attrs: {
        class: 'a_class',
        style: 'line-height: 60px; color: red;'
      },
      children: [{
        type: 'text',
        text: 'Hello&nbsp;World!'
      }],
    }],
    danmuList: [{
        text: '第 30s 出现的弹幕',
        color: '#ff0000',
        time: 30
      },
      {
        text: '第 45s 出现的弹幕',
        color: '#ff00ff',
        time: 45
      }
    ]
  },
  onLoad: function(opt) {
    console.log("Page onLoad", opt)
    util.main(app, page);
  },
  onReady: function() {
    console.log("Page onReady")
  },
  onShow: function() {
    console.log("Page onShow")
  },
  onHide: function() {
    console.log("Page onHide")
  },
  onUnload: function() {
    console.log("Page onUnload")
  },
  onPullDownRefresh: function() {
    console.log("Page onPullDownRefresh")
  },
  onReachBottom: function() {
    console.log("Page onReachBottom")
  },
  onShareAppMessage: function() {
    console.log("Page onShareAppMessage")
  },
  onPageScroll: function() {
    console.log("Page onPageScroll")
  },
  onTabItemTap: function(item) {
    console.log("Page onTabItemTap", item)
  },
  bind_tap: function(event) {
    console.log(event.type, "is", event)
  },
})