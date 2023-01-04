navigator = {}
navigator.userAgent = 'adasdasd'

navigator = new Proxy(Window,{
        get: function(target, property, receiver) {
        console.log("get: ", target, property, typeof target[property]);
        return target[property];
    },
    set: function(target, property, value) {
        console.log("set: ", target, property, value);
        return Reflect.set(...arguments);
    }
})


function ps(){
    if (navigator['userAgent']){
        return 'hello world'
    } else {
        return  ''
    }
}

console.log(ps());
// 给对象操作的时候  比如 获取 设置的时候  可以自动吐出 有哪些属性没有操作
