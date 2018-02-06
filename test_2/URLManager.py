#coding:utf-8
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()#未爬取URL集合  无序不重复元素集
        self.old_urls = set()#已爬取URL集合

    def has_new_url(self):
        '''
        判断是否有未爬取的URL
        :return:
        '''
        return self.new_url_size()!=0   #做了与运算，返回 TRUE / FALSE

    def get_new_url(self):
        '''
        获取一个未爬取的URL
        :return:
        '''
        new_url = self.new_urls.pop()  #取出一个新链接：删除列表最后一个，并返回该元素
        self.old_urls.add(new_url)     #放进就链接列表里面
        return new_url

    def add_new_url(self,url):
        '''
         将新的URL添加到未爬取的URL集合中
        :param url:单个URL
        :return:
        '''
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:   #如果连接不在未爬取链接列表并且也不再已爬取的链接列表里面，这个连接则可以加入到新链接列表里面
            self.new_urls.add(url)

    def add_new_urls(self,urls):
        '''
        将新的URLS添加到未爬取的URL集合中
        :param urls:url集合
        :return:
        '''
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)

    def new_url_size(self):
        '''
        获取未爬取URL集合的s大小
        :return:
        '''
        return len(self.new_urls)


    def old_url_size(self):
        '''
        获取已经爬取URL集合的大小
        :return:
        '''
        return len(self.old_urls)




