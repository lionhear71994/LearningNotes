# 只有有__init__.py文件的文件夹才能是package，才支持引入
import People    #引用此模块，就相当于将此模块在此处展开。
#python中一切变量都是引用变量，指向的对象包含不可变量（整型、字符串、元组）和可变量。
# 因此如果修改了不可变量，实质是新开一个空间，修改引用指向。如果修改可变量，就是保持引用指向，在原位置修改数据


# #调用模块变量、模块函数
People.set_default_age(People.default_age)    #传入12作为参数
print('=============实例化===================')
#实例化对象，开辟新内存，保留对类的引用，但是不复制属性和方法。同时调用init初始化，
#因此实例变量可以访问类变量、类方法、静态方法、实例方法。以及自己创建的实例变量。
#类对象无法访问实例变量。因为并没有一个从类对象到实例对象的指针

#实例变量可以读取的东西：类的公有属性和方法，自身的所有属性和方法。
#实例变量可以修改的东西：类对象的引用变量指向的数据,和自身的所有属性和方法
#实例变量不能修改的东西：类对象的引用变量的指向（包含属性和方法）
parent1 = People.Parent('student1')   #实例化，盗用初始化函数，创建了实例变量name和age
print('基类对象：',People.Parent.__dict__)     #打印对象的自有属性
print('基类实例对象：',parent1.__dict__)    #这一步可以看出实例化没有将类中的属性和方法引用复制到实例对象空间中。
print('==============实例对象读写数据==================')
parent1.default_name   #实例可以访问类变量，因为变量沿原型链的查找
parent1.default_name = 'Student'   #实例无法修改类变量（引用变量）的指向，所以这个是在实例对象中添加了一个实例变量
parent1.default_arr.append(1)   #实例可以修改类变量指向的数据内容
parent1.default_arr = [1,2]    #实例无法修改类变量（引用变量）的指向，所以这个是在实例对象中添加了一个实例变量
#print(parent1.__default_age)   #实例对象不能访问类对象的私有类变量
parent1.__default_age=14     #为实例对象添加实例变量（在执行时添加的不再是私有变量）
print(parent1.__default_age)  #实例对象可以访问到自身的所有属性和方法

print('基类对象：',People.Parent.__dict__)
print('基类实例对象：',parent1.__dict__)
print('=============基类对象读写数据===================')
#类对象可以访问和修改的内容：类的属性和方法
People.Parent.default_name='Student'   #修改类变量的指向
People.Parent.default_arr=[11]          #修改类变量的指向
People.Parent.default_arr.append(12)    #修改类变量指向的内容
People.Parent.__default_age=14          #通过类名无法修改私有类变量，因为在存储中私有变量的存储名为_Parent__default_age。python并不建议修改私有变量，虽然可以通过这个名称修改变量值
print('基类对象：',People.Parent.__dict__)
print('基类实例对象：',parent1.__dict__)



print('=============继承===================')
#派生类，开辟新内存，保留对基类的引用，但是不复制属性和方法。
# 因此派生类对象可以访问基类变量、基类方法、基类静态方法、基类实例方法。以及自己创建的派生类属性和方法。基类对象无法访问派生类对象。因为并没有一个从基类对象到派生类对象的指针

#派生类对象可以读取的东西：基类的公有和保护属性和方法，自身的所有属性和方法。
#派生类对象可以修改的东西：基类对象的引用变量指向的数据，和自身的所有属性和方法
#派生类不能修改的东西：基类对象的引用变量的指向（包含属性和方法）

print('基类对象：',People.Parent.__dict__)     #打印对象的自有属性
print('派生类对象：',People.Child.__dict__)    #这一步可以看出实例化没有将类中的属性和方法引用复制到实例对象空间中。
print('=============派生类对象读写数据===================')
People.Child.default_name   #派生类对象可以访问基类的类变量，因为变量沿原型链的查找
People.Child.default_name = 'child'   #派生类对象无法修改基类的类变量（引用变量）的指向，所以这个是在派生类对象中添加了一个类变量
People.Child.default_arr.append(1)   #派生类对象可以修改基类的类变量指向的数据内容
People.Child.default_arr = [1,2]    #派生类对象无法修改基类的类变量（引用变量）的指向，所以这个是在派生类对象中添加了一个类变量
# print(People.Child.__default_age)   #派生类对象不能访问基类对象的私有类变量
People.Child.__default_age=14     #为派生类对象添加类变量（在执行时添加的不再是私有变量）
print(People.Child.__default_age)  #类对象可以访问到自身的所有属性和方法

print('基类对象：',People.Parent.__dict__)
print('派生类对象：',People.Child.__dict__)
print('=============派生类的实例对象读写数据===================')
#基类的实例对象和基类的关系等同于派生类的实例对象和派生类的关系
# 派生类的初始化函数调用不会自动调用基类的初始化函数
child1 = People.Child()  #调用类的初始化函数，实例化一个对象，这里在派生类的实例对象中添加了name和age属性
child1.setname('child')  #调用派生类对象中的重写或继承的方法
# child1.getage()  #调用派生类对象添加的方法，方法访问了基类的私有变量，会报错
print('派生类对象：',People.Child.__dict__)
print('派生类实例对象：',child1.__dict__)

print('==============静态方法==================')
parent1.info()         #调用静态函数,方法1
People.Parent.info()   #调用静态函数，方法2
print('=============类方法===================')
# print(parent1.sex)   #类对象和实例对象中不存在sex，所以无法查找到，访问出错
parent1.setsex()    #调用类方法，在类对象中添加类变量
print(parent1.sex)  #通过实例对象访问类变量

print('基类对象：',People.Parent.__dict__)
print('基类实例1对象：',parent1.__dict__)


print('===========原型链查询=====================')
print(issubclass(People.Child,People.Parent)) # 布尔函数(Child,Parent)判断一个类是另一个类的子类或者子孙类，语法：issubclass(sub,sup)
print(isinstance(child1, People.Parent))  #布尔函数如果obj是Class类的实例对象或者是一个Class子类的实例对象则返回true。

