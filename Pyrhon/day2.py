#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。
#要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__,一个下划线没有被隐藏，但应视作私有属性

#判断对象类型，使用type()函数，总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。
#要获得一个对象的所有属性和方法，可以使用dir()函数
#getattr()、setattr()以及hasattr()

class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
#__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的，
#在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__

# @property的用法
class Screen(object):
    @property
    def width(self):
        return self._width
    @property
    def height(self):
        return self._height
    @width.setter
    def width(self,value):
        self._width = value
    @height.setter
    def height(self,value):
        self._height = value

    @property
    def resolution(self):
        return self._height * self._width
#测试代码
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

#__str__和__repr__
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__

#定制类：
#如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象
#然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration
#__getitem__()，__setitem__(),__delitem__()
#__getattr__
#任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用

#枚举类
print("----------------------------------------------------")
from enum import Enum,unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

@unique    #装饰器可以帮助我们检查保证没有重复值#
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

for name, member in Weekday.__members__.items():
     print(name, '=>', member)
print("--------------------------------------")

