# -*- coding: utf-8 -*-
'这是urlparse模块使用详细'

#3.0版本中已经将urllib2、urlparse、和robotparser并入了urllib中，并且修改urllib模块，其中包含5个子模块，即是help()中看到的那五个名字。

#urljoin(base,url) 拼接URL，它以base作为其基地址，然后与url中的相对地址相结合组成一个绝对URL地址
#urlsplit()
#urlunsplit()
#urlparse(url) 解析成6个部分

from urllib import parse as urlparse
#help(urlparse)

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
print(url.netloc);
new_url = urlparse.urljoin(url.netloc+'/',url.path[1:])
print(new_url);