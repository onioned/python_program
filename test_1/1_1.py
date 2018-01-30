# coding=utf-8
print 123;

print(77777);

a = 0
b = 200
print (a+b);

#缩进代码块
if a>0:
    print '大于0'
else:
    print '小于0';
    a = a+300
    print "世界";
    print a;

print "你好，世界";

str = 'Hello World!'

#字符串
print str  # 输出完整字符串
print str[0]  # 输出字符串中的第一个字符
print str[2:5]  # 输出字符串中第三个至第五个之间的字符串
print str[2:]  # 输出从第三个字符开始的字符串
print str * 3  # 输出字符串两次
print str + "TEST"  # 输出连接的字符串

#Python列表：只能通过下标访问
list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print list  # 输出完整列表
print list[0]  # 输出列表的第一个元素
print list[1:3]  # 输出第二个至第三个元素
print list[2:]  # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2  # 输出列表两次
print list + tinylist  # 打印组合的列表


#Python元组：里面元素不能修改，不过可以通过字典或者列表修改
tuple = ('runoob', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')
print tuple  # 输出完整元组
print tuple[0]  # 输出元组的第一个元素
print tuple[1:3]  # 输出第二个至第三个的元素
print tuple[2:]  # 输出从第三个开始至列表末尾的所有元素
print tinytuple * 2  # 输出元组两次
print tuple + tinytuple  # 打印组合的元组

#Python 字典：用key值访问

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print dict['one']  # 输出键为'one' 的值
print dict[2]  # 输出键为 2 的值
print tinydict  # 输出完整的字典
print tinydict.keys()  # 输出所有键
print tinydict.values()  # 输出所有值


#python 的所有数据类型都是类,可以通过 type() 查看该变量的数据类型

print type(a)
print type(list)
print type(tuple)
print type(tinydict)

'''   这是注释块
      这是注释
      这是注释
  
'''

""" 这是注释块
  这是注释块
  这是注释块
  """

#Python2.x 里，整数除整数，只能得出整数。如果要得到小数部分，把其中一个数改成浮点数即可。
print 'Python2.x 里，整数除整数，只能得出整数。如果要得到小数部分，把其中一个数改成浮点数即可。'
print (1/2)
print (1.0/2)   #把其中一个写成浮点即可
print (1/2.0)   #
print (1/float(2))   #添加类型强转也行---鼓励该方法
print (float(2))   #添加类型强转浮点类型

'''

=	简单的赋值运算符	c = a + b 将 a + b 的运算结果赋值为 c
+=	加法赋值运算符	c += a 等效于 c = c + a
-=	减法赋值运算符	c -= a 等效于 c = c - a
*=	乘法赋值运算符	c *= a 等效于 c = c * a
/=	除法赋值运算符	c /= a 等效于 c = c / a
%=	取模赋值运算符	c %= a 等效于 c = c % a
**=	幂赋值运算符	c **= a 等效于 c = c ** a
//=	取整除赋值运算符	c //= a 等效于 c = c // a

'''

a = 21
b = 10
c = 0

c = a + b
print "1 - c 的值为：", c

c += a
print "2 - c 的值为：", c

c *= a
print "3 - c 的值为：", c

c /= a
print "4 - c 的值为：", c

c = 2
c %= a
print "5 - c 的值为：", c

c **= a
print "6 - c 的值为：", c

c //= a
print "7 - c 的值为：", c


#Python位运算符  -- 需要温习位运算原理

'''
&	按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0	(a & b) 输出结果 12 ，二进制解释： 0000 1100
|	按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。	(a | b) 输出结果 61 ，二进制解释： 0011 1101
^	按位异或运算符：当两对应的二进位相异时，结果为1	(a ^ b) 输出结果 49 ，二进制解释： 0011 0001
~	按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1 。~x 类似于 -x-1	(~a ) 输出结果 -61 ，二进制解释： 1100 0011，在一个有符号二进制数的补码形式。
<<	左移动运算符：运算数的各二进位全部左移若干位，由 << 右边的数字指定了移动的位数，高位丢弃，低位补0。	a << 2 输出结果 240 ，二进制解释： 1111 0000
>>	右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，>> 右边的数字指定了移动的位数
'''

a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
c = 0

c = a & b;  # 12 = 0000 1100
print "1 - c 的值为：", c

c = a | b;  # 61 = 0011 1101
print "2 - c 的值为：", c

c = a ^ b;  # 49 = 0011 0001
print "3 - c 的值为：", c

c = ~a;  # -61 = 1100 0011
print "4 - c 的值为：", c

c = a << 2;  # 240 = 1111 0000
print "5 - c 的值为：", c

c = a >> 2;  # 15 = 0000 1111
print "6 - c 的值为：", c

print '测试github同步'

tt = 'h1h2h3h4h5h6h7h8h9';
print  tt[0:2]  #不包含2
print  tt[2]

#input()获取键盘输入的数据
#当作为数字时，则要对类型进行转换
#in_str = input('birth: ');
#new_in_str = int(in_str);  //异常：输入非数字则会报错
#print  in_str

print '测试bmi'
heigth = float(1.75)
zhong = float(80.5)
#heigth = float(input('请输入身高，（单位：米）：'))    #用键盘输入
#zhong  = float(input('请输入体重，（单位：kg）：'))    #用键盘输入
bmi = zhong / (heigth * heigth)
print '%.2f'% bmi           #保留2位小数
print '%.3f'% bmi           #保留3位小数

new_bmi = float('%.1f'% bmi)    #比较大小必须转类型
if new_bmi <18.5:
    print '过轻'
elif 18.5 <= new_bmi<25 :        #可以直接写多个与条件
    print '正常'
elif 25<= new_bmi<28 :
    print '过重'
elif 28<= new_bmi<32 :
    print '肥胖'
elif new_bmi >32:
    print '严重肥胖'

#------------------------------------------字符串拼接的方式：-----------------------------------
#1.用+拼接：
print '1.用+拼接：'
print 'A'+'B'
#2.使用%进行拼接：格式 ""%(parm,aprm)
print '2.使用%进行拼接：格式 ""%(parm,aprm) '
print 'ab %s cde %s fg' %('字符1','字符2')
# 3.使用单引号(''' ''')或者双引号(\"\"\" \"\"\")格式化字符格式
print " 3.使用单引号(''' ''')或者双引号(\"\"\" \"\"\")格式化字符格式"
print '''
a%s
b%s
c%s
d%s
'''%('字符1','字符2','字符3','字符4')


#------------------------------------------创建list--数组：-----------------------------------

print range(10)     #从0到10创建一个整数列表  range(start, stop[, step])

arr = range(10)
arr = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
#下标表达一
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#下标表达二
#[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1]
print '----------数组开始：---------'
print '基础数组：'
print arr
print '[X：Y]用法'
print arr[1:]     #从下标1开始到最后
print arr[1:5]    #从下标1开始到5
print arr[1:-1]   #从下标1开始到倒数1
print arr[-3:]    #从下标负数，还是顺序读取到最后一个元素
print arr[-3:9]   #正负2种下标都可以混合使用

print '[X：：]用法'

print arr[0::]   #即全部同等于 [X:]
print arr[1::]   #即全部
print arr[2::]   #从2开始到最后
print arr[3::]   #从3开始到最后
print arr[4::]   #从4开始到最后
print arr[-2::]   #从4开始到最后

print '[：：Y]步长为整数顺序：'
print arr[::1]     #即全部
print arr[::2]     #从左到右跳步，步长2

print '[：：Y]步长为负数倒序：'
print arr[::-1]     #即倒序，逆序
print arr[::-2]     #从右到左跳步，步长2

print '[X：：Y]步长为负数倒序：'

print arr[0::-1]   #从0逆序开始以步长1跳
print arr[1::-1]   #从1逆序开始以步长1跳
print arr[2::-1]   #从2逆序开始以步长1跳
print arr[3::-1]   #从3逆序开始以步长1跳
print arr[4::-1]   #从4逆序开始以步长1跳    4 -> 3 2 1
print '----分割线----'

print arr[0::-2]   #从0逆序开始以步长2跳
print arr[1::-2]   #从1逆序开始以步长2跳
print arr[2::-2]   #从2逆序开始以步长2跳
print arr[3::-2]   #从3逆序开始以步长2跳
print arr[4::-2]   #从4逆序开始以步长2跳    4 -> 2 0

#结论 [X ：：Y]
#1.[X：：]  等同于 [X：] 无论X为正负数，数据从X到length
#2.[：：Y]  大于0从左到右跳步(顺序)，小于0则从右到左跳步（逆序），步长Y
#3.[X ：：Y] 大于0则从X开始（包含X）从左到右跳步，小于0则从X开始从右到左跳步，步长Y

print ('----分割线 end----')

#------------------------------------------循环：-----------------------------------
#list()
#range()

print (range(5));
#print list(range(5));


for x in range(10):
    print (x);

arr = ['a','b','c','d','e']
for x in arr:
    print (x);

n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

#------------------------------------------字典(类似于对象)：-----------------------------------

#dict
print('字典：');
#初始化
dict = {
    'a':'aaa',
    'bb':'bbb',
}
#自定义：
dict['ccc'] = 'cccc';
print(dict);
print(dict['a']);

#查找某个key是否存在字典中 in 方法
print('ddd' in dict);   #false 不存在
print('a' in dict);     #true 存在

#二通过dict.get（key,【指定代表不存在参数，默认None】），不存在返回None或自定义参数,存在返回value

print(dict.get('bb'))    #返回 bbb
print(dict.get('eee'))   #返回 None   不存在

#删除值 pop(key)
dict.pop('a');
print(dict);        # 删除key为 a 的值


#------------------------------------------set：-----------------------------------

#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1);
print(s2);
print('逻辑运算:')
#或运算
print(s1 | s2);
#与运算
print(s1 & s2);
#添加元素到set中add(key)，可以重复添加，但不会有效果
s1.add(456);
print(s1);
#通过remove(key)方法可以删除元素
s1.remove(456);
print(s1);

#------------------------------------------函数定义：-----------------------------------

print('函数开始：')

def han1():
    print('hello world')

han1();


def han2():
 return 123 ,456    #返回的是tuple

ttt = han2();
print(ttt);
print(ttt[0]);
print(ttt[1]);


def add_end(L=[4,4,4]):
    L.append('END')
    print(L);
    return L


add_end([1,2,3]);   #不受影响
add_end([1,2,3]);
add_end([1,2]);
add_end();      #
add_end();      #实验证明：当默认值为可变数值，多次使用默认值，默认值会改变，（指针，引用）
                #应该避免使用可变参数作为默认值

print('默认值为可变：');

def add_end2(L=333):
    L = [];
    L.append('end')
    print(L);
    return L


add_end2();
add_end2();
add_end2();


'''def han3(a,b,c,d='dd',e):
    print('successs')

han3(1,2,3,4)  '''     #SyntaxError: non-default argument follows default argument  不能把默认值写在非默认值前面，引起异议，默认值写在后面

def han3(a,b,c,d='dd',e='ee'):
    print('successs')

han3(1,2,3,);
han3(1,2,3,4);
han3(1,2,3,e='fff');    #多个默认值，直接用表达式，可跳过前面的默认值

'''------------------可变参数------------------
说明：可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
'''

def han4(*number):      #number 为元组,只能定义一个这样的参数
    print(number);      #输出：(1,2,3)

han4(1)
han4(1,2,3)

temp = [4,5,6];
temp2 = (7,8,9);
han4(*temp);            #使用list
han4(*temp2);           #使用tuple

'''#han4(*temp2,111,222);   #不能在后面加其余的参数------ 写后面则不知道那个参数对应哪个
'''

def han4_4(a,b,*temp):          #运行参数写在可变参数前面
    print('a=', a);
    print('b=', b);
    print('temp=', temp);
    pass

han4_4(1,2,3,4,5);          #4,5,6 组装成tuple
han4_4(1,2,*temp);          #使用list
han4_4(1,2,*temp2);         #使用tuple


'''
def han5(*number,*number2):     #不能写2个可变参数  
    print(number);       
'''

'''------------------关键字参数------------------
说明：键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict （类似于对象）
'''

def han6(a,b,**c):          #必须输入dict(对象)
    print('a=',a);
    print('b=',b);
    print('c=',c);          #输出：'c=', {}


han6(1,2);
han6(1,2,ccc='ccc');        #输出： 'c=', {'ccc': 'ccc'}
han6(1,2,ccc={'q':'q','w':'w'});

han6(1,2,c={'q1':'q'},e='eee');


#han6(1,2,{'q1':'q','w1':'w'});     #必须带参数名

han6(1,2,**{'q1':'q','w1':'w'});  #直接使用dict，带上 **


#temp3 = {'a':'a111','s':'ssss2'}  #键名key 不能跟 参数列表本身重复

temp3 = {'a1':'a111','s1':'ssss2'}

han6(1,2,**temp3);                  #直接使用dict，带上 **


'''------------------命名关键字参数------------------
说明：   如果要限制关键字参数的名字，即为参数必须定义该参数的意思，就可以用命名关键字参数 fun( a,b,*,d,e),*后面的参数就是要限制的参数；
        d和e必须以dict（key=value）的方式定义
'''

'''
def han7(a,b,*,c,d):        python2 居然不支持
    pass
    
def f1(a, b, c=0, *args, **kw):
    pass    
    
'''


'''------------------总结：------------------

*args:随意参数，普通参数，list，tuple
**kw：dict-键对值



'''

'''------------------切片------------------
list :[]
tuple : ()
字符串
以上都能切片

'''

print ('ABCDEFG'[:3])

#L = (range(100));   #创建 0~100的列表
#print(L);

L = []

#循环
for i in range(0,99):
    L.append(i)

L = (range(100));

print  L[0];
print  L[0:20];
print  L[0:20];
print  L[:10:2];  #前10个数，每2各取一个
print  L[:];

'''------------------迭代 -- 循环------------------
'''

for i in 'ABC':    #字符串
    pass

for i in [1,2,3]:    #list
    pass

for i in (1,2,3):    #tuple
    pass

d = {'a':1,'b':2}

for key in d:               #遍历dict 的 key
    pass

for value in {}.values():    #dict 的 values
    pass

for k, v in d.items():      #dict 的key, values
    pass

'''------------------列表生成式------------------
 
 [表达式  for x in 列表 条件 ]
 【占用空间呢】
'''

print '分割线------------';

print [x * x for x in range(1, 11)]

print [x * x for x in range(1, 11) if x % 2 == 0 if x % 3 == 0]  #?：允许多个条件，那条件怎么算

print [m + n for m in 'ABC' for n in 'XYZ']   #嵌套

'''------------------生成器------------------
这种一边循环一边计算的机制，称为生成器：generator
【不占用空间】
generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。

创建一个generator，第一种方法：列表生成式的[]改成()，
generator也是可迭代对象 Iterable
 
'''

(x * x for x in range(10))

'''------------------迭代器------------------
 
我们已经知道，可以直接作用于for循环的数据类型有以下几种：

一类是集合数据类型，如list、tuple、dict、set、str等；

一类是generator，包括生成器和带yield的generator function。

这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。

可以使用isinstance()判断一个对象是否是Iterable对象：


1.list、dict、str虽然是Iterable，却不是Iterator

2.生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了。

可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator，表示一个惰性计算的序列

3.转换成Iterator，使用iter()函数


'''


'''------------------高级函数------------------
把函数作为参数的函数叫高级函数
map(f,[])：  #循环数组里面每个元素并按照f函数规则生成一个全新的列表，返回新的 Iterator
def f(x):
  return x * x
map(f,[x1,x2,x3]) 

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])  
list(r)
结果：[1, 4, 9, 16, 25, 36, 49, 64, 81]  
r是惰性序列，需要用list(),把全部值计算出来

reduce(f,[]) #f必须接受2个参数，reduce把结果和序列的下一个元素做运算,返回不是 Iterator

reduce(f, [x1, x2, x3, x4]) 

   ==> t = f(x1,x2)
        ==> t2 = f(t,x3)
            ==> t3 = = f(t2,x4)
            ......



'''














'''------------题外：递归函数---------------'''

def han8(year=1,sum=0):
        # print(sum)
         if year > 20:
             print(sum)
             return
         else:
             sum = (sum + 1) * 1.2
             year = year + 1
             han8(year, sum)
han8()


x = 1.2
for i in range(0,19):
    y=(x+1)*0.2 + 1+x
    x=y

print(1.2 + x)



'''---------------------------'''







