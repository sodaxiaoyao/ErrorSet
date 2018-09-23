Page({
  data: {
    animationData: {}
  },
  onShow: function() {
    this._dom_api();
    this._animation_api();
  },
  _dom_api: function() {

    var query = wx.createSelectorQuery().in(this);
    query.select("#test").boundingClientRect(function(rect) {
      console.log(rect);
    }).exec();

    query.selectAll("#test").fields({
      properties: ['scrollX', 'scrollY'],
      computedStyle: ['margin', 'backgroundColor']
    }, function(res) {
      console.log(res);
    }).exec()

    query.selectViewport().scrollOffset(function(res) {
      console.log(res);
    }).exec();


    wx.createIntersectionObserver().relativeToViewport({
      bottom: 100
    }).observe('#anim', (res) => {
      console.log("接触", res);
    });

  },
  _animation_api: function() {

    var animation = wx.createAnimation({
      transformOrigin: "50% 50% 0",
      duration: 400,
      timingFunction: "linear",
      delay: 0
    });

    animation.opacity(0.2).step();
    animation.backgroundColor("blue").step();
    animation.width(200).step();
    animation.height(800).step();
    animation.top(700).step();
    animation.left(30).step();
    animation.bottom(20).step();
    animation.right(50).step();

    // 更多变换请看文档

    this.setData({
      animationData: animation.export()
    })


  }
})