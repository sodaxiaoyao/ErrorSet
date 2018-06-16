let page = getCurrentPages();
let app = getApp();
let util = require("../UtilsTest/UtilsTest.js");
Page({
  data: {
    data_test: "data_test_data",
    data_test_array: [...Array(5).keys()],
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