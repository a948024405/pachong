
function proxy (proxy_array) {
    for (let i=0; i<proxy_array.length; i++){
        eval(proxy_array[i] + `= new Proxy(` + proxy_array[i] + `, {
            get(target, key) {
             // debugger;
              console.log('----------------------')
              console.log( '获取了：'+ '` + proxy_array[i] + `'+'的' + key + '属性,详细位置可以debugger查看');
              console.log('----------------------')
              return target[key];
            }
        });`)
    }
}

navigator = {}
window = {}
location = {}
navigator.userAgent = 'adasdasdasdas'

var proxy_array = ['window', 'navigator','location'];
proxy(proxy_array)



function ps(){
    if (navigator['userAgent']){
        console.log('asdasdsa')
    }
    if (zs['pn']){
        return 'xxxx'
    }
}
document = {}
// console.log(ps());
console.log(document.toString());
 //  node [object Object]    浏览器  '[object HTMLDocument]'
// 什么地方停止 去补谁就可以了
var object_toStrint = Object.prototype.toString()
Object.prototype.toString = function (){
    // [object HTMLDocument]
    let _xxx = object_toStrint.call(this, arguments);
    console.log(this)

}