# -*- coding: utf-8 -*-
'这是类的学习'

class Student():
    def __init__(self,name,score):  #1.初始化

        self.name = name;           #2.外部可以访问,public
        self.score = score;
        self.__p_name = name;       #3.  __修饰，表示私有 private
        self.__p_score = score;
    def print_score(self):
        print('%s %s' % (self.name,self.score));
        print('%s %s' % (self.__p_name,self.__p_score));


stu = Student(123,345);
stu.print_score();
#print (stu.name);      #可以读取 public
#print (stu.__p_name);  #不能读取 private

stu.name2 = 456;          #4. 可以重新增加新属性变量，注意是public
stu.__name3 = 789;        #不同与内部私有变量，不能外部修改或者新增私有，只是单纯新增一个公有的属性变量  public
print (stu.name2);
print (stu.__name3);


'''-----------多态---------
多态意思就是“多种状态”。接口的多种不同的实现方式即为多态。
子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态，即获得父类的run()方法，也可以获得自己的方法。
外部调用原则：先调用子类的方法，当无，则尝试调用父类方法。
'''

class Animal(object):
    name = 'Animal';               #定义自己的属性
    def run(self):
        print('Animal is running');
    def run2(self,):
       pass;


class Dog(Animal):                  #继承Animal类
    name = 'Dog';                   # 定义自己的属性
    def run(self):                  #子类的run()覆盖了父类的run()
        print('Dog is running');


class Cat(Animal):
    name = 'Cat';                   # 定义自己的属性
    def run(self):
        print('Cat is running');

cat = Cat();
cat.run();



class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')




class Tortoise2(Animal):
    def run2(self):         #当子类找不到对于的方法，则会向父类找
        print('Tortoiseeeeee is running slowly...')


#多态的体现
def run_twice(animal):              #根据传入的类，调用该类对应的方法.原则：按照先找子类再找父类
    animal.run()                    #来自于子类继承父类重写的方法，也就是说父子类公共的方法
    animal.run()


run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
run_twice(Tortoise())
run_twice(Tortoise2())

an = Animal();
an.run2();


'''------------------总结----------------

由于Python是动态语言，所以，传递给函数 run_twice(animal)的参数 animal 不一定是 Animal 或 Animal 的子类型。任何数据类型的实例都可以，run_twice()的方法即可：
这是动态语言和静态语言（例如Java）最大的差别之一。动态语言调用实例方法，不检查类型，只要方法存在，参数正确，就可以调用。

java检查类型，需要父类数据类型的引用指向子类对象。
  Animal am = new Cat();

2要素：
1.存在继承关系
2、子类要重写父类的方法
 
'''

'''-------------------使用__slots__----------------------
:限制class实例能添加的属性

'''
print('使用__slots__')

class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

s = Student() # 创建新的实例
s.name = 'Michael' # 绑定属性'name'
s.age = 25 # 绑定属性'age'
#s.score = 99  # 绑定属性'score' , score被限制了


'''-------------------使用@property----------------------
@property装饰器就是负责把一个方法变成属性调用的

'''


'''-------------------多重继承----------------------
让子类拥有更多父类的功能-------水平拓展，不是纵向拓展（树）
通常：：MixIn

'''

class Other(Animal):            #警告：不能把存在继承关系的类写在一起 class Other(Animal,Dog,Cat):  是错误的，原因：既然有继承关系，通过子类也可以使用父类的功能
    def parm(self):
        print(Animal.name);


#如此，Other就拥有 Animal,Dog,Cat 的所有功能


o = Other();
o.parm();


class Other2(Dog,Cat):
    def parm(self):
        print(Animal.name);         #调用父类Animal的功能
        print(Dog.name);
        print(Cat.name);

o = Other2();
o.parm();


'''-------------------定制类----------------------
__str__

__iter__

__getitem__

__getattr__

__call__

'''

'''---------------------使用枚举类------------------------


'''


