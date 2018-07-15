onmessage = function (e) {
    // importScripts();
    let num = e.data;
    console.log("传进来", num);
    let sum = 0;
    for (let i = 0; i < num; i++) {
        sum += i;
    }
    postMessage(sum);
    close();
};
