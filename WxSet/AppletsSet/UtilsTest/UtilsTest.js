function main(a, p) {
  console.log("APP Info", a);
  console.log("Page Info", p);
  wx_api();
}

function wx_api() {
  console.log("执行wx api");




  console.log("==============API request======================");
  let requestTask = wx.request({
    url: 'http://localhost/',
    data: {
      'test': 'hello,server'
    },
    header: {
      'content-type': 'application/x-www-form-urlencoded'
    },
    method: "POST",
    dataType: "json",
    responseType: "text",
    success: function(res) {
      console.log("wx.request success", res);
    },
    fail: function(res) {
      console.log("wx.request fail", res);
    },
    complete: function(res) {
      console.log("wx.request complete", res);
    }
  });
  // requestTask.abort();





  console.log("==============API uploadFile======================");
  if (0)
    wx.chooseImage({
      success: function(res) {
        let uploadTask = wx.uploadFile({
          url: 'http://localhost/',
          filePath: res.tempFilePaths[0],
          name: 'file',
          header: {},
          formData: {
            'user': 'test_formData'
          },
          success: function(res) {
            console.log("wx.uploadFile success", res);
          },
          fail: function(res) {
            console.log("wx.uploadFile fail", res);
          },
          complete: function(res) {
            console.log("wx.uploadFile complete", res);
          }
        });
        uploadTask.onProgressUpdate((res) => {
          console.log('上传进度', res.progress)
          console.log('已经上传的数据长度', res.totalBytesSent)
          console.log('预期需要上传的数据总长度', res.totalBytesExpectedToSend)
        });
        // uploadTask.abort();
      }
    });




  console.log("==============API downloadFile======================");
  let downloadTask = wx.downloadFile({
    url: 'http://localhost/static/images/up_images/test.jpg',
    header: {},
    success: function(res) {
      console.log("wx.downloadFile success", res);
    },
    fail: function(res) {
      console.log("wx.downloadFile fail", res);
    },
    complete: function(res) {
      console.log("wx.downloadFile complete", res);
    }
  });
  downloadTask.onProgressUpdate((res) => {
    console.log('下载进度', res.progress)
    console.log('已经下载的数据长度', res.totalBytesWritten)
    console.log('预期需要下载的数据总长度', res.totalBytesExpectedToWrite)
  })
  // downloadTask.abort();






  console.log("==============API onSocketError======================");
  wx.onSocketError(function(res) {
    console.log("wx.onSocketError", res);
  });




  console.log("==============API onSocketMessage======================");
  wx.onSocketMessage(function(res) {
    console.log("wx.onSocketMessage", res);
  });




  console.log("==============API onSocketOpen======================");
  wx.onSocketOpen(function(res) {
    console.log("wx.onSocketOpen", res);
    send_msg();
  });




  console.log("==============API onSocketClose======================");
  wx.onSocketClose(function(res) {
    console.log("wx.onSocketClose", res);
  });





  console.log("==============API connectSocket======================");
  let SocketTask=wx.connectSocket({
    url: 'ws://localhost/web_socket',
    header: {},
    method: "GET",
    success: function(res) {
      console.log("wx.connectSocket success", res);
    },
    fail: function(res) {
      console.log("wx.connectSocket fail", res);
    },
    complete: function(res) {
      console.log("wx.connectSocket complete", res);
    }
  });


  console.log("==============API sendSocketMessage======================");
  function send_msg() {
    wx.sendSocketMessage({
      data: "hello,server",
      success: function(res) {
        console.log("wx.sendSocketMessage success", res);
      },
      fail: function(res) {
        console.log("wx.sendSocketMessage fail", res);
      },
      complete: function(res) {
        console.log("wx.sendSocketMessage complete", res);
      }
    });
  }



  console.log("==============API closeSocket======================");
  wx.closeSocket();


  console.log("==============API chooseImage======================");


}

module.exports = {
  main: main
}