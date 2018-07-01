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
        // previewImage(res.tempFilePaths);
        getImageInfo(res);
        // saveImageToPhotosAlbum(res.tempFilePaths[0]);
        saveFile(res);
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

  console.log("==============API saveImageToPhotosAlbum======================");

  function saveImageToPhotosAlbum(path) {
    wx.saveImageToPhotosAlbum({
      filePath: path,
      success: function(res) {
        console.log("wx.saveImageToPhotosAlbum success", res);
      },
      fail: function(res) {
        console.log("wx.saveImageToPhotosAlbum fail", res);
      },
      complete: function(res) {
        console.log("wx.saveImageToPhotosAlbum complete", res);
      }
    })
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




  console.log("==============API getAvailableAudioSources======================");
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
  if (0)
    wx.chooseVideo({
      sourceType: ['album', 'camera'],
      compressed: true,
      maxDuration: 60,
      success: function(res) {
        console.log("wx.chooseVideo success", res);
        saveVideoToPhotosAlbum(res);
      },
      fail: function(res) {
        console.log("wx.chooseVideo fail", res);
      },
      complete: function(res) {
        console.log("wx.chooseVideo complete", res);
      }
    });




  console.log("==============API saveVideoToPhotosAlbum======================");

  function saveVideoToPhotosAlbum(_res) {
    wx.saveVideoToPhotosAlbum({
      filePath: _res.tempFilePath,
      success: function(res) {
        console.log("wx.saveVideoToPhotosAlbum success", res);
      },
      fail: function(res) {
        console.log("wx.saveVideoToPhotosAlbum fail", res);
      },
      complete: function(res) {
        console.log("wx.saveVideoToPhotosAlbum complete", res);
      }
    });
  }





  console.log("==============API createVideoContext======================");
  if (0)
    createVideoContext();

  function createVideoContext() {
    let videoContext = wx.createVideoContext('myVideo', this);

    videoContext.play();
    videoContext.seek(80);
    setTimeout(function() {
      videoContext.sendDanmu({
        "text": "asdf",
        "color": "red"
      });
      videoContext.pause();
    }, 3000);
    videoContext.playbackRate(1.5);
    videoContext.requestFullScreen();
    videoContext.exitFullScreen();
  }



  console.log("==============API createCameraContext======================");

  function createCameraContext() {
    let cameraContext = wx.createCameraContext(this);
    cameraContext.startRecord({
      timeoutCallback: function(res) {
        console.log("cameraContext.startRecord timeoutCallback", res);
      },
      success: function(res) {
        console.log("cameraContext.startRecord success", res);
      },
      fail: function(res) {
        console.log("cameraContext.startRecord fail", res);
      },
      complete: function(res) {
        console.log("cameraContext.startRecord complete", res);
      }
    });
    cameraContext.stopRecord({
      success: function(res) {
        console.log("cameraContext.stopRecord success", res);
      },
      fail: function(res) {
        console.log("cameraContext.stopRecord fail", res);
      },
      complete: function(res) {
        console.log("cameraContext.stopRecord complete", res);
      }
    });
    cameraContext.takePhoto({
      quality: "high",
      success: function(res) {
        console.log("cameraContext.takePhoto success", res);
      },
      fail: function(res) {
        console.log("cameraContext.takePhoto fail", res);
      },
      complete: function(res) {
        console.log("cameraContext.takePhoto complete", res);
      }
    });
  }




  console.log("==============API loadFontFace======================");
  if (0)
    wx.loadFontFace({
      family: 'Bitstream Vera Serif Bold',
      source: 'url("http://developer.mozilla.org/@api/deki/files/2934/=VeraSeBd.ttf")',
      desc: {
        "style": "normal",
        "weight": "normal",
        "variant": "normal ",
      },
      success: function(res) {
        console.log("wx.loadFontFace success", res);
      },
      fail: function(res) {
        console.log("wx.loadFontFace fail", res)
      },
      complete: function(res) {
        console.log("wx.loadFontFace complete", res);
      }
    });




  console.log("==============API saveFile======================");

  function saveFile(_res) {
    getFileInfo(_res.tempFilePaths[0]);
    wx.saveFile({
      tempFilePath: _res.tempFilePaths[0],
      success: function(res) {
        console.log("wx.saveFile success", res);
        getSavedFileList();
      },
      fail: function(res) {
        console.log("wx.saveFile fail", res)
      },
      complete: function(res) {
        console.log("wx.saveFile complete", res);
      }
    });
  }




  console.log("==============API getFileInfo======================");

  function getFileInfo(path) {
    wx.getFileInfo({
      filePath: path,
      digestAlgorithm: "md5",
      success: function(res) {
        console.log("wx.getFileInfo success", res);
      },
      fail: function(res) {
        console.log("wx.getFileInfo fail", res)
      },
      complete: function(res) {
        console.log("wx.getFileInfo complete", res);
      }
    })
  }





  console.log("==============API getSavedFileList======================");

  function getSavedFileList() {
    wx.getSavedFileList({
      success: function(res) {
        console.log("wx.getSavedFileList success", res);
        getSavedFileInfo(res.fileList[0].filePath);
        removeSavedFile(res.fileList[0].filePath);
      },
      fail: function(res) {
        console.log("wx.getSavedFileList fail", res)
      },
      complete: function(res) {
        console.log("wx.getSavedFileList complete", res);
      }
    })
  }





  console.log("==============API getSavedFileInfo======================");

  function getSavedFileInfo(path) {
    wx.getSavedFileInfo({
      filePath: path,
      success: function(res) {
        console.log("wx.getSavedFileInfo success", res);
      },
      fail: function(res) {
        console.log("wx.getSavedFileInfo fail", res)
      },
      complete: function(res) {
        console.log("wx.getSavedFileInfo complete", res);
      }
    })
  }


  console.log("==============API removeSavedFile======================");

  function removeSavedFile(path) {
    wx.removeSavedFile({
      filePath: path,
      success: function(res) {
        console.log("wx.removeSavedFile success", res);
      },
      fail: function(res) {
        console.log("wx.removeSavedFile fail", res)
      },
      complete: function(res) {
        console.log("wx.removeSavedFile complete", res);
      }
    });
  }




  console.log("==============API openDocument======================");

  function openDocument(path) {
    wx.openDocument({
      filePath: path,
      fileType: "doc",
      success: function(res) {
        console.log("wx.openDocument success", res);
      },
      fail: function(res) {
        console.log("wx.openDocument fail", res)
      },
      complete: function(res) {
        console.log("wx.openDocument complete", res);
      }
    })
  }




  console.log("==============API setStorage======================");
  wx.setStorage({
    key: "key",
    data: "value",
    success: function(res) {
      console.log("wx.setStorage success", res);
    },
    fail: function(res) {
      console.log("wx.setStorage fail", res)
    },
    complete: function(res) {
      console.log("wx.setStorage complete", res);
    }
  })




  console.log("==============API setStorageSync======================");
  try {
    wx.setStorageSync('key1', 'value1');
  } catch (e) {
    console.log(e);
  }



  console.log("==============API getStorage======================");
  wx.getStorage({
    key: 'key1',
    success: function(res) {
      console.log("wx.getStorage success", res);
    },
    fail: function(res) {
      console.log("wx.getStorage fail", res)
    },
    complete: function(res) {
      console.log("wx.getStorage complete", res);
    }
  });



  console.log("==============API getStorageSync======================");
  try {
    console.log("wx.getStorageSync", wx.getStorageSync('key1'));
  } catch (e) {
    console.log(e);
  }


  console.log("==============API getStorageInfo======================");
  wx.getStorageInfo({
    success: function(res) {
      console.log("wx.getStorageInfo success", res);
    },
    fail: function(res) {
      console.log("wx.getStorageInfo fail", res)
    },
    complete: function(res) {
      console.log("wx.getStorageInfo complete", res);
    }
  })



  console.log("==============API getStorageInfoSync======================");
  try {
    var res = wx.getStorageInfoSync()
    console.log("wx.getStorageInfoSync", res.keys);
    console.log("wx.getStorageInfoSync", res.currentSize);
    console.log("wx.getStorageInfoSync", res.limitSize);
  } catch (e) {
    console.log(e);
  }




  console.log("==============API removeStorage======================");
  wx.removeStorage({
    key: "key1",
    success: function(res) {
      console.log("wx.removeStorage success", res);
    },
    fail: function(res) {
      console.log("wx.removeStorage fail", res)
    },
    complete: function(res) {
      console.log("wx.removeStorage complete", res);
    }
  });






  console.log("==============API removeStorageSync======================");
  try {
    wx.removeStorageSync('key');
  } catch (e) {
    console.log(e);
  }







  console.log("==============API clearStorage======================");
  wx.clearStorage();






  console.log("==============API clearStorage======================");
  try {
    wx.clearStorageSync();
  } catch (e) {
    conosole.log(e);
  }




  console.log("==============API getLocation======================");
  wx.getLocation({
    type: "wgs84",
    altitude: true,
    success: function(res) {
      console.log("wx.getLocation success", res);
    },
    fail: function(res) {
      console.log("wx.getLocation fail", res)
    },
    complete: function(res) {
      console.log("wx.getLocation complete", res);
    }
  });



  console.log("==============API chooseLocation======================");
  if (0)
    wx.chooseLocation({
      success: function(res) {
        console.log("wx.chooseLocation success", res);
      },
      fail: function(res) {
        console.log("wx.chooseLocation fail", res)
      },
      complete: function(res) {
        console.log("wx.chooseLocation complete", res);
      }
    });




  console.log("==============API openLocation======================");
  if (0)
    wx.getLocation({
      type: 'gcj02',
      success: function(res) {
        wx.openLocation({
          latitude: res.latitude,
          longitude: res.longitude,
          scale: 28,
          name: "测试",
          address: "地址详细说明",
          success: function(res) {
            console.log("wx.openLocation success", res);
          },
          fail: function(res) {
            console.log("wx.openLocation fail", res)
          },
          complete: function(res) {
            console.log("wx.openLocation complete", res);
          }
        })
      }
    });




  console.log("==============API createMapContext======================");
  if (0)
    createMapContext();

  function createMapContext() {
    let mapContext = wx.createMapContext("myMap", this);

    mapContext.getCenterLocation({
      success: function(res) {
        console.log("mapContext.getCenterLocation success", res);
      },
      fail: function(res) {
        console.log("mapContext.getCenterLocation fail", res)
      },
      complete: function(res) {
        console.log("mapContext.getCenterLocation complete", res);
      }
    });


    mapContext.moveToLocation();


    mapContext.translateMarker({
      markerId: 1,
      destination: {
        latitude: 23.10229,
        longitude: 113.3345211,
      },
      autoRotate: true,
      rotate: 30,
      duration: 1000,
      animationEnd: function() {
        console.log("mapContext.translateMarker animationEnd");
      },
      fail: function() {
        console.log("mapContext.translateMarker fail");
      }
    });


    mapContext.includePoints({
      points: [{
        longitude: '116.481451',
        latitude: '40.006822'
      }, {
        longitude: '116.487847',
        latitude: '40.002607'
      }, {
        longitude: '116.496507',
        latitude: '40.006103'
      }],
      padding: [10, 10, 10, 10]
    });


    mapContext.getRegion({
      success: function(res) {
        console.log("mapContext.getRegion success", res);
      },
      fail: function(res) {
        console.log("mapContext.getRegion fail", res)
      },
      complete: function(res) {
        console.log("mapContext.getRegion complete", res);
      }
    });


    mapContext.getScale({
      success: function(res) {
        console.log("mapContext.getScale success", res);
      },
      fail: function(res) {
        console.log("mapContext.getScale fail", res)
      },
      complete: function(res) {
        console.log("mapContext.getScale complete", res);
      }
    });
  }





  console.log("==============API getSystemInfo======================");
  










}

module.exports = {
  main: main
}