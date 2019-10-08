参考资料：[菜鸟教程jQuery实例](https://www.runoob.com/jquery/jquery-examples.html)
### jQuery语法
```javascript
$(selector).action()
$("p")      //元素选择器
$("#id")    //id选择器
$(".class") //类选择器
```
### 操作DOM
```javascript
text()      //获取text
html()      //获取html
val()       //获取输入值
attr()      //获取属性值
```
### AJAX
AJAX是与服务器交换数据的技术，它在不重载全部页面的情况下，实现了对部分网页的更新。
```javascript
$(selector).load(URL,data,callback);
```
* 必需的 URL 参数规定您希望加载的 URL。
* 可选的 data 参数规定与请求一同发送的查询字符串键/值对集合。
* 可选的 callback 参数是 load() 方法完成后所执行的函数名称。
```javascript
$.post(URL,data,callback); 
```
* 必需的 URL 参数规定您希望请求的 URL。
* 可选的 data 参数规定连同请求发送的数据。
* 可选的 callback 参数是请求成功后所执行的函数名。
