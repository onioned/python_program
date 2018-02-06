#coding:utf-8
import re
#import urlparse        #3.0版本中已经将urllib2、urlparse、和robotparser并入了urllib中，并且修改urllib模块，其中包含5个子模块，即是help()中看到的那五个名字。
from urllib import parse as urlparse

#help(urlparse)

from bs4 import BeautifulSoup


class HtmlParser(object):

    def parser(self,page_url,html_cont):
        '''
        用于解析网页内容抽取URL和数据
        :param page_url: 下载页面的URL
        :param html_cont: 下载的网页内容
        :return:返回URL和数据
        '''
        if page_url is None or html_cont is None:
            return
        #soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')        #from_encoding='utf-8'参数失效
        soup = BeautifulSoup(html_cont,'html.parser')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        #print(new_urls)
        #print(new_data)
        return new_urls,new_data


    def _get_new_urls(self,page_url,soup):
        '''
        抽取新的URL集合
        :param page_url: 下载页面的URL
        :param soup:soup
        :return: 返回新的URL集合
        '''
        new_urls = set()
        #抽取符合要求的a标签
        #原书代码
        # links = soup.find_all('a',href=re.compile(r'/view/\d+\.htm'))
        #2017-07-03 更新,原因百度词条的链接形式发生改变
        #links = soup.find_all('a', href=re.compile(r'/item/.*'))    #相对路径的地址  搜索当前tag的所有tag子节点,并判断是否符合过滤器的条件
        links = soup.find_all('a', href=re.compile(r'/item/.*'))    #相对路径的地址  .* 后面匹配任何字符
        #print(links);
        #print(type(links)); #返回的是 list

        for link in links:
           #print(link);
           #print(link.href);
           # print(link['href']);       #获取soup对象的指定数据
           # print(link['target']);
            #提取href属性
            new_url = link['href']
            #拼接成完整网址
            new_full_url = urlparse.urljoin(page_url,new_url)   #以page_url为基地址，拼接上相对路径，最后获取完整链接
            new_urls.add(new_full_url)
        return new_urls
    def _get_new_data(self,page_url,soup):
        '''
        抽取有效数据
        :param page_url:下载页面的URL
        :param soup:
        :return:返回有效数据
        '''
        data={}
        data['url']=page_url
        title = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        data['title']=title.get_text()
        summary = soup.find('div',class_='lemma-summary')
        #获取到tag中包含的所有文版内容包括子孙tag中的内容,并将结果作为Unicode字符串返回
        data['summary']=summary.get_text()
        return data
