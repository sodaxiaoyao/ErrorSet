// pages/index/index.js
var tool = require('../../utils/util.js');
var app = getApp();

Page({
  data: {
    user_info:{
      "name":"zyp",
      "phone":"13601129109",
      "address":"北京市通州区"
    }
  },
  onLoad: function () {
    console.log(tool.get_content(app.globalData["hello"]));
  }
})
