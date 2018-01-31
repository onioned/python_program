
# -*- coding: utf-8 -*-
'''
print ('ABCDEFG'[:3])

L = range(0, 30);
print(L);


for i in L:
    print(i);


L = list(range(20));

print(L);

for i in L:
    print(i);

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




'''------------------高级函数 map reduce lambda  filter------------------
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

lambda 用于支持将函数赋值给变量的一个操作符 默认是返回的,所以不用再加return关键字,不然会报错，关键字lambda表示匿名函数
result = lambda x: x * x            #定义了1个参数x
result = lambda x,y: x * y          #定义了2个参数x,y
result = lambda : 2 * 5             #不定义参数
result = lambda : x * y             #不定义参数，但x,y必须有上面代码提供
result(2)       # 输出：4

def a(a):
    b = lambda x: x * a     #将函数赋值给变量，本身不会运算，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
    print(b(a));            #得到运算结果
    print(b);               #得到函数体
    return b

print(a(3));

def build(x, y):
    return lambda: x * x + y * y        #此处无需定义参数，因为外面有


filter()函数用于过滤序列 ,把传入的函数依次作用于每个元素作为判别条件，然后根据返回值是True还是False决定保留还是丢弃该元素


sorted()函数就可以对list进行排序，接收一个key函数来实现自定义的排序
数值：由小到大
字符串：ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面
传入第三个参数reverse=True ： 反序
'''

# lambda 无需参数，直接使用外部参数
def build(x, y):
    f = lambda: x * x + y * y;
    return f()                  #无需参数，参数有上面提供直接使用

# lambda 需要参数，外部提供参数
def build2(x, y):
    f = lambda x,y: x * x + y * y;
    return f(x,y)               #需要参数，由拷贝上面的参数使用

print ('build=',build(1,2));
print ('build2=',build2(1,2));



#用filter求素数

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def ttt(x,n):
    return x % n > 0

def _not_divisible(n):
    return lambda x: x % n > 0      ###此处返回一个函数体，而不是一个返回值
    #return ttt(x,n)


def primes():
    yield 2
    it = _odd_iter() # 初始序列
    print('it=xx',it);          #只执行一次
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)      # 构造新序列,筛选惰性序列
                                                    # lambda x: x % 3 > 0
                                                    # lambda x: x % 5 > 0
                                                    # lambda x: x % 7> 0

#打印1000以内的素数:
for n in primes():
 if n < 10:
     print(n)
 else:
     break


#sorted（[],key = fun, reverse=True、false） 排序
#key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序.  --- 2步走

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)] 
#按照字符串排序
def by_name(t):
    return t[0] #根据元素返回的数据再进行排序

#按照数字排序
def by_name2(t):
    return t[1]

L2 = sorted(L, key=by_name)
print(L2)

L2 = sorted(L, key=by_name2)
print(L2)

L2 = sorted(L, key=by_name2, reverse=True)      # reverse=True 反序
print(L2)


'''--------------------返回函数-----------------------
高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回

'''