const assert = require('assert').strict;
const child_process = require('child_process');
const cluster = require('cluster');


//========================================断言=================================================
assert(1 === 1);
const {message} = new assert.AssertionError({
    actual: 1,
    expected: 2,
    operator: 'equal'
});
console.log({message});

assert.equal(1, 1);
assert.deepEqual(1, 1);
(async () => {
    await assert.doesNotReject(async () => {
    }, SyntaxError);
})();
assert.doesNotThrow(() => {
});
assert.ifError(null);

assert.ok(1);
// assert.fail("失败");

assert.notEqual({a: 1}, {a: '1'});
assert.notDeepEqual({a: 1}, {a: '1'});
(async () => {
    await assert.rejects(async () => {
        throw new TypeError('错误信息');
    }, {name: 'TypeError', message: '错误信息'});
})();
assert.throws(() => {
    throw new TypeError('错误信息');
});


//========================================缓冲=================================================
const buf1 = Buffer.alloc(10);
const buf2 = Buffer.alloc(10, 1);
const buf3 = Buffer.allocUnsafe(10);
buf3.fill(0);
const buf8 = Buffer.allocUnsafeSlow(10);
buf8.fill(0);
const buf4 = Buffer.from([1, 2, 3]);
const buf5 = Buffer.from('test', 'ascii');
const buf6 = Buffer.from('test', 'latin1');
// ascii|utf8|utf16le|ucs2|base64|latin1|binary|hex

// const buf7 = new Buffer(10);
// 从 Node.js 8.0.0 开始， Buffer(num) 和 new Buffer(num) 将返回一个初始化内存之后的 Buffer。

console.log(buf5.toString('hex'));
console.log(buf5.toString('base64'));

const arr = new Uint16Array(2);
arr[0] = 5000;
arr[1] = 4000;

// 拷贝 `arr` 的内容
const buf9 = Buffer.from(arr);
// 与 `arr` 共享内存
const buf10 = Buffer.from(arr.buffer, 0, 2);
console.log(buf9);
console.log(buf10);
console.log(buf10.length);

arr[1] = 6000;
console.log(buf9);
console.log(buf10);

const str = '\u00bd + \u00bc = \u00be';
// 输出: ½ + ¼ = ¾: 9 个字符, 12 个字节
console.log(`${str}: ${str.length} 个字符, ` +
    `${Buffer.byteLength(str, 'utf8')} 个字节`);

const buf11 = Buffer.from('1234');
const buf12 = Buffer.from('0123');
const arr1 = [buf1, buf2];
console.log(arr1.sort(Buffer.compare));

const buf13 = Buffer.alloc(10);
const buf14 = Buffer.alloc(14);
const buf15 = Buffer.alloc(18);
const totalLength = buf13.length + buf14.length + buf15.length;
// 输出: 42
console.log(totalLength);
const bufA = Buffer.concat([buf13, buf14, buf15], totalLength);
// 输出: <Buffer 00 00 00 00 ...>
console.log(bufA);
// 输出: 42
console.log(bufA.length);
console.log(Buffer.isBuffer(bufA));
console.log(Buffer.isEncoding("utf8"));
console.log(Buffer.poolSize);
console.log(buf11.toString('ascii'));

const arrayBuffer = new ArrayBuffer(16);
const buffer = Buffer.from(arrayBuffer);
console.log(buffer.buffer === arrayBuffer);


const bufB = Buffer.allocUnsafe(26);
const bufC = Buffer.allocUnsafe(26).fill('!');
for (let i = 0; i < 26; i++) {
    bufB[i] = i + 97;
}
bufB.copy(bufC, 8, 16, 20);
console.log(bufB.toString('ascii', 0, 25));

const bufD = Buffer.from('buffer');
for (const pair of bufD.entries()) {
    console.log(String.fromCharCode(pair[1]));
}


console.log(buf1.equals(buf2));
console.log(bufD.includes("u"));
console.log(bufD.indexOf("u"));
console.log(bufD.keys());
console.log(bufD.lastIndexOf("u"));
console.log(bufD.length);
console.log(bufD.values());


//========================================子进程=================================================
child_process.exec("node --version", {
    encoding: 'utf8',
    timeout: 0,
    maxBuffer: 200 * 1024,
    killSignal: 'SIGTERM',
    cwd: null,
    env: null
}, (error, stdout, stderr) => {
    if (error) {
        console.error(`exec error: ${error}`);
        return;
    }
    console.log(`stdout: ${stdout}`);
    console.log(`stderr: ${stderr}`);
});

child_process.execFile('node', ['--version'], (error, stdout, stderr) => {
    if (error) {
        throw error;
    }
    console.log("execFile");
    console.log(stdout);
    console.log(stderr);
});

// const  n = child_process.fork( `./sub.js`);
// n.on( 'message', (m) => {
//     console.log( 'PARENT got message:',  m);
// });
// n.send({ hello:  'world' });
//sub.js
// process.on( 'message', (m) => {
//     console.log( 'CHILD got message:',  m);
// });
// process.send({ foo:  'bar' });

const version = child_process.spawn('node', ["--version"]);
version.stdout.on('data', (data) => {
    console.log(`输出：${data}`);
});
version.stderr.on('data', (data) => {
    console.log(`错误：${data}`);
});
version.on('error', (err) => {
    console.log('启动子进程失败。',err);
});
version.on('close', (code) => {
    console.log(`子进程退出码：${code}`);
});
console.log("进程目录",process.argv0);

// child_process.spawn()、child_process.fork()、child_process.exec() 和 child_process.execFile()
// 函数都遵循 Node.js API 惯用的异步编程模式。

// child_process.spawnSync()、child_process.execSync() 和 child_process.execFileSync()
// 方法是同步的且会阻塞 Node.js 的事件循环，暂停任何额外代码的执行直到衍生的进程退出。

console.log("子进程通道",version.channel);
console.log("连接性",version.connected);
console.log("句柄",version.pid);


//========================================集群=================================================
if (cluster.isMaster) {
    console.log(`主进程 ${process.pid} 正在运行`);
    cluster.on('exit', (worker, code, signal) => {
        console.log(`工作进程 ${worker.process.pid} 已退出`);
    });
}


//========================================控制台=================================================
console.log('你好%s','世界');
console.error(new Error('错误信息'));
const name = '描述';
console.warn(`警告${name}`);

// const myConsole = new console.Console(out, err);
// myConsole.log('你好世界');
// // 打印: '你好世界'到 out。
// myConsole.log('你好%s', '世界');
// // 打印: '你好世界'到 out。
// myConsole.error(new Error('错误信息'));
// // 打印: [Error: 错误信息]到 err。
// myConsole.warn(`警告${name}`);
// // 打印: '警告描述'到 err。