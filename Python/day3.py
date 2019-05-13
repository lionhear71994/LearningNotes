#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，
#而是直接跳转至错误处理代码，即except语句块，执行完except后，如果有finally语句块，则执行finally语句块
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!' #assert语句本身就会抛出AssertionError,启动Python解释器时可以用-O参数来关闭assert
    return 10 / n

def main():
    foo('0')

'''
import logging
logging.basicConfig(level=logging.INFO) #允许你指定记录信息的级别，有debug，info，warning，error等几个级别
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
'''

#文档测试：
#if __name__=='__main__':
#    import doctest
#    doctest.testmod()

#IO:
#同步和异步的区别就在于是否等待IO执行的结果
'''
with open('/path/to/file', 'r') as f:
    print(f.read())
    
with open('/Users/michael/test.txt', 'w') as f:
    f.write('Hello, world!')    

'''

# StringIO  BytesIO
'''
import os
print(os.environ.get("PATH"))
print(os.path.abspath('.'))
print(os.path.join('/Users/michael', 'testdir'))
print(os.path.split('/Users/michael/testdir/file.txt'))
print(os.path.splitext('/path/to/file.txt'))
print("------------------------------------------")
os.mkdir os.rmdir os.rename os.remove
shutil模块提供了copyfile()的函数,它们可以看做是os模块的补充
'''

#不重要。因为不兼容：Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容
#pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object
#我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象

#dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。
#要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化
import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
#print(json.dumps(s))     TypeError: Object of type 'Student' is not JSON serializable
print(json.dumps(s, default=lambda obj: obj.__dict__))
print("-----------------------------------------------")










