App({
  onLaunch: function (opt) {
    console.log("APP onLaunch", opt);
  },
  onShow: function (opt) {
    console.log("APP onShow", opt);
  },
  onHide: function () {
    console.log("APP onHide");
  },
  onError: function (msg) {
    console.log("APP onError", msg);
  },
  onPageNotFound: function () {
    console.log("APP onPageNotFound");
  },
  globalData: {
    global_data_test: "global_data_test"
  }
})
