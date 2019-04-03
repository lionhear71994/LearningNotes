#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#五种参数：位置参数，默认参数，可变参数，关键字参数，命名关键字参数
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。

f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

#列表生成式
print('--------------------------------------')
print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])

#生成器：如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
g = (x * x for x in range(10))
#凡是可作用于for循环的对象都是Iterable类型；
#凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
#集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

#高阶函数:
#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
#filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
#sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)

#返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
#关键字lambda表示匿名函数，冒号前面的x表示函数参数。匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
#用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数

#函数对象有一个__name__属性，可以拿到函数的名字
#装饰器:
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)     #decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'，有些依赖函数签名的代码执行就会出错。
                                   #原始函数的__name__等属性复制到wrapper()函数中，Python内置的functools.wraps就是干这个事的。
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log("excute")
def now():
    print("2018-4-10")
print("--------------------------------------")
now()
print(now.__name__)

#偏函数：functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
int2 = functools.partial(int, base=2)

#私有方法格式： _xxx()






