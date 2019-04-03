__all__=["default_age","default","Moniter"]            # __all__变量，设置导入模块import*时将会自动引入的函数、变量、类
default_age = 12                                          #定义模块变量
def set_default_age(age=13):                               #定义模块函数
    print("默认年龄为"+str(age)+"岁")


class Parent(object):                                  #定义模块类。()内指定基类，当是object可以省略不写
    print("定义了Student类")                          #定义类时就会执行内部的执行语句
    default_name='student'                             #定义一个类变量(不可修改变量)
    default_arr = []                                    #定义一个类变量(可修改变量)
    __default_age=12                                    #函数名或属性名前面为双下划线表示成员私有。只能在当前类或对象空间内使用。在存储时是存储成_Parent__default_age
    def __init__(self, name1='student1',age1=13):     #init是构造函数，self代表类的实例对象。参数可以设置默认值。
        self.name=name1                                 #自动新增两个实例变量
        self.age=age1
        print("基类构造函数设置了"+self.name)
    def getname(self):                                  #实例方法,函数名为引用变量，可以进行赋值,即变更函数体。函数引用变量调用时使用()，不带括号代表变量。getname代表函数引用变量，getname()代表代表调用函数
        print('基类读取名称'+self.name)
        return self.name
    def setname(self,name1):
        self.name=name1
        print("基类设置名称"+self.name)

    @staticmethod                                         # @staticmethod声明函数为静态方法，通过类对象和实例对象直接调用
    def info():                                          #静态方法就像类外函数一样。如果函数内需要读写类变量，需要使用Parent.default_name
        print("派生类的静态函数"+Parent.default_name)

    @classmethod  # @classmethod声明函数为类方法，第一个参数是能是类对象的引用，可以通过类或者实例直用
    def setsex(self):  # 类方法self表示对类的引用
        self.sex = '男'  # 添加类变量
        print("派生类设置性别" + self.sex)

# 派生类继承了基类的类变量和类方法和实例方法（没有实例变量，因为实例变量是在实例以后才存在的）
class Child(Parent):                            #生成派生类，可以多重继承，但是应尽量避免。继承后会包含基类的函数和特性。
    def __init__(self,name1="child"):          #派生类构造函数不会自动调用基类构造函数
        self.name = name1                       #在当前实例对象中新增name实例变量
        Parent.__init__(self)                   #两种方法，调用超类的构造函数。基类中就修改了name实例变量，新增了age实例变量
        # super(Child,self).__init__(name1)
        print("派生类构造函数"+self.name)                #这里读取的就是最后一次对name的修改（基类中对他的修改）

    def setname(self, name1):                           #重写基类中的方法。其实是在派生类中添加了一个新方法，因此在查找此函数时就必用向上查找了。
        self.name = "新"+name1
        print("基类设置名称" + self.name)

    def getage(self):                                   #派生类添加新的实例方法
        pass
        #print("派生类读取年龄"+str(self.__default_age)) #派生类是无法读取基类的私有类变量的。因此这句话会报错



print('Peopeo类开始运行')    #导入模块或执行模块都会执行函数

# 当一个module被执行时,moduel.__name__的值将是"__main__",而当一个 module被其它module引用时，module.__name__将是module自己的名字
if __name__=="__main__":     #只有在执行当前模块时才会运行此函数
    set_default_age()

