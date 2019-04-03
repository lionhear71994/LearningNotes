#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
面向对象
'''
class player:
    sex = "male"     #类变量

    def play(self):                     #实例方法第一个定义的参数必须是实例对象本身
        print(id(self),"+ 成员方法")

    @classmethod                         #第一个参数一定是类的引用，不过可以通过类或者实例的引用
    def handle(self):
        print(id(self),"+ 类方法")

    @staticmethod
    def staticplay():                #没有默认的必须参数
        print("静态方法")
'''
uzi = player()
uzi.play()
print(id(uzi))
print("--------------------------------------------------------")
player.handle()
print(id(player))
print("--------------------------------------------------------")
player.staticplay()                         #通过类调用
mlxg = player()
mlxg.staticplay()                           #通过实例调用
print("--------------------------------------------------------")
'''
'''
Python内置的类属性
__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
__doc__ :类的文档字符串
__name__: 类名
__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
__bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）
'''
'''
Python内置的类方法
__init__ 构造函数，在生成对象时调用
__del__ 析构函数，释放对象时使用
__repr__ 打印，转换
__setitem__按照索引赋值
__getitem__按照索引获取值
__len__获得长度
__cmp__比较运算
__call__函数调用
__add__加运算
__sub__减运算
__mul__乘运算
__div__除运算
__mod__求余运算
__pow__称方
'''
'''
#我们可以为这些函数进行重写，实现我们想要的功能。例如这里对所有的读写操作进行监督屏蔽。
def __getitem__(self,key):                 #在字典中获取值时会自动调用 __getitem__函数，设置值时会自动调用__setitem__函数
    print("-------------派生类字典读取值")
def __setitem__(self,key,value):
    print("-------------派生类字典设置值")
def __getattr__(self,name):               #读取类属性（包括继承的属性）会自动执行__getattr__函数，设置属性会自动执行__setattr__函数
    print("-------------读取派生类属性")
def __setattr__(self,name,value):
    print("-------------设置派生类属性值")
'''
'''
python中继承中的一些特点：
1：在继承中基类的构造（__init__()方法）不会被自动调用，它需要在其派生类的构造中亲自专门调用。
2：在调用基类的方法时，需要加上基类的类名前缀，且需要带上self参数变量。区别于在类中调用普通函数时并不需要带上self参数。
3：Python总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。（先在本类中查找调用的方法，找不到才去基类中找）。
'''

#运算符重载 def __add__(self, other):
#        return Vector(self.a + other.a, self.b + other.b)


