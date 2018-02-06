# -*- coding: utf-8 -*-
'这是BeautifulSoup模块使用详细'

'''
解析下载回来的html内容

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_cont,'html.parser')               #解析内容
links = soup.find_all('a', href=re.compile(r'/item/.*'))    #获取执行的标签
for link in links:                                          #循环出数据
    #提取href属性
    new_url = link['href']


'''


