
// 目标对象（被代理对象）
var target = {
    name: 'JACK',
    age: 18,
};

// 代理行为对象（对目标对象进行取值或赋值行为时，会进入此对象的方法）
var handler = {
    get: function(target, property, receiver) {
        console.log("get: ", target, property, typeof target[property]);
        return target[property];
    },
    set: function(target, property, value) {
        console.log("set: ", target, property, value);
        return Reflect.set(...arguments);
    }
};

// 使用 Proxy 构造函数实例出新的target对象
var targets = new Proxy(target, handler)
console.log(targets.age);



// navigator.userAgent = 'asdasd'  // set
// navigator['userAgent']  // get
// navigator.userAgent  // get

// 混淆 可变的参数才可以混淆  什么东西不可变  new document window   aaa = '张三' bbb ='lisi'




