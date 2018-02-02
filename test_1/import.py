# -*- coding: utf-8 -*-
'这是引入模块的学习'

import math             #引入整个math包

print(math)
print(math.pi)


from math import pi     #引入math包的pi类，适用于引用单个类

print(pi)

'''-------------------引用根目录模块文件-------------------'''

import function                         #加载整个模块文件

function.import_fun()

from function import import_fun         #加载整个模块文件的某一个类，函数，变量等等

import_fun()

from module import Test                 #引用module模块的Test类

test = Test()


'''-------------------引用其他目录的模块文件2种写法-------------------'''


from test import hello                      #引用test目录下hello模块

print(hello.parm)


from test.hello  import parm                #引用test下hello模块的parm参数

print(parm)







