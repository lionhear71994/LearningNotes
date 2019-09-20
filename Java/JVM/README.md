### 运行时数据区域  
##### 线程私有的：
    程序计数器：  指令顺序，跟随线程生命。  
    虚拟机栈：  跟随线程生命，方法数据由此传递，StackOverFlowError和OOM，栈帧。
    本地方法栈：  类似上，执行Native方法。
##### 线程共享的：
    堆：  绝大多数对象实例和数组。
    方法区：  类、常量、静态变量等数据。
		运行时常量池：  基本数据类型值、字符串、final；全限定名、方法描述符、字段描述符。1.8后移至Heap内。

### 虚拟机对象  
##### 对象的创建