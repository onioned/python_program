# -*- coding: utf-8 -*-
'这是urlparse模块使用详细'

#3.0版本中已经将urllib2、urlparse、和robotparser并入了urllib中，并且修改urllib模块，其中包含5个子模块，即是help()中看到的那五个名字。

#urlsplit()    返回一个包含5个字符串项目的元组：协议、位置、路径、查询、片段。 urlsplit()和urlparse()差不多。不过它不切分URL的参数
#urlunsplit() 使用urlsplit()返回的值组合成一个url


from urllib import parse as urlparse
#help(urlparse)


#urlparse(url) 解析成6个部分
url=urlparse.urlparse('https://www.baidu.com/index.php')
print(url)

'''
返回：字典子类，要用.调用
ParseResult(scheme='https', netloc='www.baidu.com', path='/index.php', params='', query='', fragment='')

scheme	0	协议	空字符串

netloc	1	服务器地址	空字符串	
path	2	路径	空字符串	
parameters	3	参数	空字符串	
query	4	查询部分	空字符串	
fragment	5	分片部分	空字符串	
username	
用户名	None	
password	
密码	None	
hostname	
主机名	None	
port	
端口	None
'''

#urljoin(base,url) 拼接URL，它以base作为其基地址，然后与url中的相对地址相结合组成一个绝对URL地址

print(url.scheme);
print(url.netloc);
print(url.path);
new_url = urlparse.urljoin(url.netloc+'/',url.path[1:])     # netloc开头不加http,结尾不加/，拼接失败
print(url.path);
new_url = urlparse.urljoin(url.netloc+'/',url.path[1:])
print(new_url);
new_url = urlparse.urljoin('http://'+url.netloc,url.path)
print(new_url);
'''正确用法：'''
new_url = urlparse.urljoin(url.scheme+'://'+url.netloc,url.path)
print(new_url);

url=urlparse.urljoin('http://www.baidu.com','index.html')
print(url);

