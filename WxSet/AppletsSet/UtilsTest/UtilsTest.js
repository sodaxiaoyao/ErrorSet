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
  let SocketTask = wx.connectSocket({
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
  if (0)
    wx.chooseImage({
      count: 1,
      sizeType: ['original', 'compressed'],
      sourceType: ['album', 'camera'],
      success: function(res) {
        console.log("wx.chooseImage success", res);
        previewImage(res.tempFilePaths);
        getImageInfo(res);
        saveImageToPhotosAlbum(res.tempFilePaths[0]);
      },
      fail: function(res) {
        console.log("wx.chooseImage fail", res);
      },
      complete: function(res) {
        console.log("wx.chooseImage complete", res);
      }
    });



  console.log("==============API previewImage======================");

  function previewImage(urls) {
    wx.previewImage({
      current: urls[0],
      urls: urls,
      success: function(res) {
        console.log("wx.previewImage success", res);
      },
      fail: function(res) {
        console.log("wx.previewImage fail", res);
      },
      complete: function(res) {
        console.log("wx.previewImage complete", res);
      }
    });
  }



  console.log("==============API getImageInfo======================");

  function getImageInfo(img) {
    wx.getImageInfo({
      src: img.tempFilePaths[0],
      success: function(res) {
        console.log("wx.getImageInfo success", res);
      },
      fail: function(res) {
        console.log("wx.getImageInfo fail", res);
      },
      complete: function(res) {
        console.log("wx.getImageInfo complete", res);
      }
    });
  }



  console.log("==============API getRecorderManager======================");
  let recorderManager = wx.getRecorderManager();
  recorderManager.start({
    duration: 10000,
    sampleRate: 16000,
    numberOfChannels: 1,
    encodeBitRate: 25000,
    format: "mp3",
    frameSize: 1,
    audioSource: "auto",
  });
  recorderManager.pause();
  recorderManager.resume();
  // recorderManager.stop();

  recorderManager.onStart(function() {
    console.log("recorderManager.onStart");
  });
  recorderManager.onPause(function() {
    console.log("recorderManager.onPause");
  });
  recorderManager.onStop(function(res) {
    console.log("recorderManager.onStop", res);
  });
  recorderManager.onFrameRecorded(function(res) {
    console.log("recorderManager.onFrameRecorded", res);
  });
  recorderManager.onError(function(res) {
    console.log("recorderManager.onError", res);
  });



  console.log("==============API getBackgroundAudioManager======================");
  if (0)
    getBackgroundAudioManager();

  function getBackgroundAudioManager() {
    let backgroundAudioManager = wx.getBackgroundAudioManager();

    // 读写
    backgroundAudioManager.src = 'http://ws.stream.qqmusic.qq.com/M500001VfvsJ21xFqb.mp3?guid=ffffffff82def4af4b12b3cd9337d5e7&uin=346897220&vkey=6292F51E1E384E061FF02C31F716658E5C81F5594D561F2E88B854E81CAAB7806D5E4F103E55D33C16F3FAC506D1AB172DE8600B37E43FAD&fromtag=46';
    backgroundAudioManager.startTime = 3;
    backgroundAudioManager.title = '此时此刻';
    backgroundAudioManager.epname = '此时此刻';
    backgroundAudioManager.singer = '许巍';
    backgroundAudioManager.coverImgUrl = 'http://y.gtimg.cn/music/photo_new/T002R300x300M000003rsKF44GyaSk.jpg?max_age=2592000';
    backgroundAudioManager.webUrl = 'http://www.zyp233.cn';
    backgroundAudioManager.protocol = 'http';

    backgroundAudioManager.onCanplay(function() {
      console.log("backgroundAudioManager.onCanplay");
    });
    backgroundAudioManager.onPlay(function() {
      console.log("backgroundAudioManager.onPlay");
      // 只读
      console.log("backgroundAudioManager.duration", backgroundAudioManager.duration);
      console.log("backgroundAudioManager.currentTime", backgroundAudioManager.currentTime);
      console.log("backgroundAudioManager.paused", backgroundAudioManager.paused);
      console.log("backgroundAudioManager.buffered", backgroundAudioManager.buffered);
      // 方法
      backgroundAudioManager.play();
      backgroundAudioManager.pause();
      backgroundAudioManager.seek(30);
      backgroundAudioManager.stop();
    });
    backgroundAudioManager.onPause(function() {
      console.log("backgroundAudioManager.onPause");
    });
    backgroundAudioManager.onStop(function() {
      console.log("backgroundAudioManager.onStop");
    });
    backgroundAudioManager.onEnded(function() {
      console.log("backgroundAudioManager.onEnded");
    });
    backgroundAudioManager.onTimeUpdate(function() {
      console.log("backgroundAudioManager.onTimeUpdate");
    });
    backgroundAudioManager.onError(function(res) {
      console.log("backgroundAudioManager.onError", res);
    });
    backgroundAudioManager.onWaiting(function() {
      console.log("backgroundAudioManager.onWaiting");
    });
  }




  console.log("==============API createInnerAudioContext======================");
  if (0)
    createInnerAudioContext();

  function createInnerAudioContext() {
    let innerAudioContext = wx.createInnerAudioContext();

    innerAudioContext.src = 'http://ws.stream.qqmusic.qq.com/M500001VfvsJ21xFqb.mp3?guid=ffffffff82def4af4b12b3cd9337d5e7&uin=346897220&vkey=6292F51E1E384E061FF02C31F716658E5C81F5594D561F2E88B854E81CAAB7806D5E4F103E55D33C16F3FAC506D1AB172DE8600B37E43FAD&fromtag=46';
    innerAudioContext.startTime = 30;
    innerAudioContext.autoplay = true;
    innerAudioContext.loop = true;
    innerAudioContext.obeyMuteSwitch = false;
    innerAudioContext.volume = 0.3;

    innerAudioContext.onCanplay(function() {});
    innerAudioContext.onPlay(function() {
      console.log("innerAudioContext.duration", innerAudioContext.duration);
      console.log("innerAudioContext.currentTime", innerAudioContext.currentTime);
      console.log("innerAudioContext.paused", innerAudioContext.paused);
      console.log("innerAudioContext.buffered", innerAudioContext.buffered);
    });
    innerAudioContext.onPause(function() {});
    innerAudioContext.onStop(function() {});
    innerAudioContext.onEnded(function() {});
    innerAudioContext.onTimeUpdate(function() {});
    innerAudioContext.onError(function() {});
    innerAudioContext.onWaiting(function() {});
    innerAudioContext.onSeeking(function() {});
    innerAudioContext.onSeeked(function() {});

    // innerAudioContext.offCanplay(function(){});
    // innerAudioContext.offPlay(function () { });
    // innerAudioContext.offPause(function () { });
    // innerAudioContext.offStop(function () { });
    // innerAudioContext.offEnded(function () { });
    // innerAudioContext.offTimeUpdate(function () { });
    // innerAudioContext.offError(function () { });
    // innerAudioContext.offWaiting(function () { });
    // innerAudioContext.offSeeking(function () { });
    // innerAudioContext.offSeeked(function () { });
  }


  console.log("==============API createInnerAudioContext======================");
  wx.getAvailableAudioSources({
    success: function(res) {
      console.log("wx.getAvailableAudioSources success", res);
    },
    fail: function(res) {
      console.log("wx.getAvailableAudioSources fail", res);
    },
    complete: function(res) {
      console.log("wx.getAvailableAudioSources complete", res);
    }
  });



  console.log("==============API chooseVideo======================");
  


}

module.exports = {
  main: main
}