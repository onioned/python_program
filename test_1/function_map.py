# -*- coding: utf-8 -*-
'这是内置函数汇总'

#dict(); 创建一个字典
d = dict(a='a', b='b', t='t')
print(d);

#set():  函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等
print(set([1,1,2,3,4]))  #重复1被删除

print(set(['a','b','c','d','e','f','f',]))  #重复f被删除

x = set([1,2,3,4,5,9])
y = set([0,3,4,5,6,7,8])

print(x & y)    #与，交集

print(x | y)    #或，并集

print(x - y)    #非，差集

print(y - x)    #非，差集

'''------------字典------------ '''

#字典.pop():  删除字典给定键 key 所对应的值，返回值为被删除的值  字典--对象

#dict.pop(key) : key不能为空，返回key对应的value
a = {'a':123,'b':456}
print(a)
b = a.pop('a');
print(b)            #value
print(a)            #已经被修改过的字典--对象


'''------------列表------------ '''

#列表.pop():  移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。

#列表.pop(【可选下标，默认最后一个】):  返回从列表中移除的元素对象

l = ['a','b','c','d','e','f','g']

print(l)
print(l[2:5])       #下标5不要
print(l.pop())      #删除最后一个
print(l.pop(1))     #删除下标2的元素
print(l)
print(l[0])
print(l[1])



'''------------ set ------------ '''
# :基本数据类型的一种集合类型，可以是列表，字典，字符串
#set集合是无序的，不能通过索引和切片来做一些操作,不重复

#增加：
# add(parm):把parm作为整体添加到集合里面
a = set();
a.add('add')
print(a)

# update(parm):把parm拆解成每个组成部分，添加都集合里面
a.update('update');
print(a)
a.update([1,2,3]);
print(a)
a.update({'aa':11,'bb':2});
print(a)

#删除


'''------------ requests 模块 ------------'''

import requests
