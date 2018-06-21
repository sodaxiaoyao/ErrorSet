Page({
  data: {
    x: 0,
    y: 0,
  },
  onReady: function() {



    //创建ctx
    const ctx = wx.createCanvasContext('firstCanvas', this);




    //图片
    ctx.drawImage("../images/ImageTest.jpg", 0, 0, 300, 150);
    const pattern = ctx.createPattern('../images/ImageTest.jpg', 'repeat-x');
    ctx.fillStyle = pattern;



    //创建渐变器
    ctx.beginPath();
    // let grd = ctx.createLinearGradient(0, 0, 200, 0);
    let grd = ctx.createCircularGradient(80, 55, 60);
    grd.addColorStop(0, 'red');
    grd.addColorStop(0.16, 'orange');
    grd.addColorStop(0.33, 'yellow');
    grd.addColorStop(0.5, 'green');
    grd.addColorStop(0.66, 'cyan');
    grd.addColorStop(0.83, 'blue');
    grd.addColorStop(1, 'purple');



    //设置样式
    // ctx.setTransform(scaleX, skewX, skewY, scaleY, translateX, translateY);
    ctx.scale(0.5, 0.5);
    ctx.rotate(20 * Math.PI / 180);
    ctx.translate(20, 20);
    ctx.setFontSize(20);
    ctx.setLineDash([20, 30], 0);
    ctx.lineDashOffset = 0;
    ctx.setShadow(2, 2, 3, 'white');
    // ctx.setTextAlign("center");
    ctx.textAlign = "center";
    // ctx.setTextBaseline("middle");
    ctx.textBaseline = "middle";
    // ctx.setLineWidth(2);
    ctx.lineWidth = 15;
    // ctx.setLineCap("round");
    ctx.lineCap = "round";
    // ctx.setLineJoin("miter");
    ctx.lineJoin = "miter";
    // ctx.setMiterLimit(5);
    ctx.miterLimit = 5;
    // ctx.setGlobalAlpha(0.2);
    ctx.globalAlpha = 0.3;
    ctx.globalCompositeOperation = "lighter";




    //填充
    // ctx.setFillStyle(grd);
    ctx.fillStyle = grd;
    // ctx.rect(30, 30, 100, 50);
    // ctx.fill();
    ctx.fillRect(30, 30, 100, 50);
    ctx.fillText('Hello', 20, 20);
    const metrics = ctx.measureText('Hello World');
    console.log("measureText", metrics);




    //描绘
    ctx.beginPath();
    // ctx.setStrokeStyle(grd);
    ctx.strokeStyle = "red";
    ctx.font = '68px Arial';
    ctx.strokeText("zyp", 0, 300);
    ctx.strokeRect(130, 120, 30, 30);
    ctx.moveTo(50, 250);
    ctx.lineTo(50, 300);
    ctx.lineTo(80, 300);
    ctx.closePath();

    ctx.stroke();



    //曲线
    ctx.beginPath();
    ctx.arc(100, 75, 50, 0, 1.5 * Math.PI, false);
    ctx.arcTo(200, 200, 100, 100, 10);
    ctx.bezierCurveTo(20, 300, 200, 100, 200, 20);
    ctx.quadraticCurveTo(20, 100, 200, 20);
    ctx.stroke();



    //弧
    ctx.beginPath();
    ctx.setStrokeStyle("red");
    ctx.moveTo(100, 20);
    ctx.arcTo(150, 20, 150, 70, 50);
    ctx.stroke();




    //清除和裁剪
    ctx.clearRect(0, 80, 150, 75);
    ctx.clip();
    ctx.save();
    ctx.restore();




    //绘制
    ctx.draw(false, function(res) {
      console.log(res)
    });




    wx.canvasGetImageData({
      canvasId: 'firstCanvas',
      x: 30,
      y: 30,
      width: 100,
      height: 50,
      success(res) {
        console.log(res.data);
        put_img(res.data);
      },
      fail: function(res) {
        console.log(res);
      },
      complete: function(res) {
        console.log(res);
      }
    }, this);


    function put_img(data) {
      wx.canvasPutImageData({
        canvasId: 'firstCanvas',
        data: data,
        x: 160,
        y: 30,
        width: 100,
        height: 50,
        success: function(res) {
          console.log(res);
        },
        fail: function(res) {
          console.log(res);
        },
        complete: function(res) {
          console.log(res);
        }
      }, this);
    }
  },

  do_Cstart: function(event) {
    if (0)
      wx.canvasToTempFilePath({
        x: 0,
        y: 0,
        width: 300,
        height: 300,
        destWidth: 300,
        destHeight: 300,
        canvasId: 'firstCanvas',
        fileType: "png",
        quality: 1,
        success: function(res) {
          console.log(res.tempFilePath);
          wx.previewImage({
            urls: [res.tempFilePath]
          })
        },
        fail: function(res) {
          console.log(res);
        },
        complete: function(res) {
          console.log(res);
        }
      }, this);
  },
  do_Cmove: function(event) {
    this.setData({
      x: event.touches[0].clientX,
      y: event.touches[0].clientY,
    });
  },

})