# -*- coding: utf-8 -*-
'这是BeautifulSoup模块使用详细'

'''
<<<<<<< HEAD
https://cuiqingcai.com/1319.html
从HTML或XML文件中提取数据的Python库

BeautifulSoup(markup, "html.parser")  #markup为html的内容

'''

from bs4 import BeautifulSoup

#help(BeautifulSoup)
=======
解析下载回来的html内容

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_cont,'html.parser')               #解析内容
links = soup.find_all('a', href=re.compile(r'/item/.*'))    #获取执行的标签
for link in links:                                          #循环出数据
    #提取href属性
    new_url = link['href']


'''
>>>>>>> 2f72f4620c1984841d2319074516224acc4084d4


