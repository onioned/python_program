# -*- coding: utf-8 -*-
'这是正则学习'



# \d 匹配一个数字
# \w 匹配一个字母或者数字
# \s 匹配一个空格（也包括Tab等空白符）
# .  匹配除换行符以外的任意字符
# \b 匹配单词的开头和结尾
#  ^ 行里面的开头
#  $ 行里面的结束
# .* 匹配任何字符字符不限数量

#反义
# \D 匹配非数字的字符,非\d
# \W
# \S
# \B
#[^规则] 反义匹配
#[^a] 匹配除了a以外的字符
#[^abcde] 匹配除了a,b,c,d,e以外的字符
#[^(123|abc)] 匹配除了1,2,3 或者 a,b,c以外的字符


#匹配数量
# *表示任意个字符（包括0个）
# +表示至少一个字符
# ?表示0个或1个字符
# {n}表示n个字符
# {n,}表示n个字符或更多
# {n,m}表示n-m个字符


# [] 字符集合即：不使用预设代码: \d \s \w 等等，自定义规则
# [0-9]
# [a-z]
# [A-Z]
# [0-9a-zA-Z\_] 匹配数字，大小字母，下划线；\为转义
# [0-9a-zA-Z\_]* 匹配以上条件，不限数量
# [a-zA-Z\_][0-9a-zA-Z\_]* 匹配前面条件为一个，后面条件不限
# [a-zA-Z\_][0-9a-zA-Z\_]{0, 19} 匹配后者条件 0-19个；实际限制（前面1个字符+后面最多19个字符）= 20个字符

'''
1. 条件1条件2条件3 数量 
2.[条件1，条件2，条件3] 数量

1表示所有条件全匹配，然后接数量限制
    条件1 数量 与
    条件2 数量 与
    条件3 数量
    
2.表示所有条件接数量限制，即为：
    条件1  数量 或
    条件2  数量 或
    条件3  数量



'''


# | 分支条件
# A|B 匹配A或者B
# (a|b)ython 匹配 aython 或者 bython

# ( ) 分组，作为一个整体
# (abc[0-3]\.){3}  abc 接 0~3 接 . ,重复3次： abc0.abc0.abc0.
'''常用分组形式
捕获：
(exp) 匹配exp，并捕获文本到自动命名的组里
(?<name>exp) 匹配exp，并捕获文本到 name 的组里,可以写成 (?'name'exp)
(?:exp) 匹配exp，不捕获内容，不分组，常用校验

零宽断言：
(?=exp)
(?<=exp)
(?!exp)
(?<!exp)

注释：
(?#comment)

'''






# ^ 匹配行的开头
# ^\d 必须以数字开头

# $ 匹配行的结束
# \d$ 表示必须以数字结束

# ^py$   限制了行开头和结尾，只能匹配 py 字符，精确匹配


'''每个/为一组正则'''

# \d{3}\s+\d{3,8}  ： 匹配 xxx xxxxxxxx 为格式的字符串
# 空格换成 - ： \d{3}\-\d{3,8}  -要用\转义  ： 匹配 xxx-xxxxxxxx 为格式的字符串



import re  #加载正则模块

s = r'ABC\\-001'             #r 修饰正则，可免转义符号
print(re.match(s,'ABC')) #None 问题： \转义有点问题
print(re.match(s,'ABC\-001')) #None 问题： \转义有点问题

s = r'\\-'
print(re.match(s,'\-')) #None 问题：  \转义有点问题

s=r'/item/.*'
s = re.match(s,'/item/-001')
print(s)



test = '用户输入的字符串'
if re.match(r'用户输入的字符串', test):
    print('ok')
else:
    print('failed')


'''----------正则切割字符串----------
str.split('切割字符')        返回list []
re.split('正则表达式',str)   返回list []
正则一般用上 []

'''

s = 'a b   c'.split(' ')
print(s)

s = 'a b   c'.split(r'\s+')
print(s)

#re.split(正则,字符串) 只要符合正则就可以分割出来

s = re.split(r'\s+','a b   c')
print(s)

s = re.split(r'[\s\,]+','a,b, c   d')
print(s)

s = re.split(r'[\s,]+','a,b, c   d')        #在r修饰下，不转义也行，建议使用转义，养成好的习惯
print(s)

s = re.split(r'[\s\;\,]+', 'a,b;; c  d')   #只要符合[]里一个条件即可分割出来
print(s)


'''----------使用re.compile----------

1. 使用re.compile 比普通的要有效率

re模块中包含一个重要函数是compile(pattern [, flags]) ，该函数根据包含的正则表达式的字符串创建模式对象。可以实现更有效率的匹配。在直接使用字符串表示的正则表达式进行search,match和findall操作时，python会将字符串转换为正则表达式对象。而使用compile完成一次转换之后，在每次使用模式的时候就不用重复转换。当然，使用re.compile()函数进行转换后，re.search(pattern, string)的调用方式就转换为 pattern.search(string)的调用方式。

'''

print('compile：')
#需要转换正则对象
s = re.split(r'\s+','a b   c')
print(s)

#不需要转换正则对象
reObj = re.compile(r'\s+')
s = reObj.split('a b   c');
print(s)




