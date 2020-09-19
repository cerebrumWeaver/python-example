from random import randint
import requests 
import random
from time import sleep
from bs4 import BeautifulSoup
from lxml import etree

# 'https://www.baidu.com/s?wd=https%3A%2F%2Fblog.csdn.net%2Fpoweiliuxing%2Farticle%2Fdetails%2F108582616&rsv_spt=1&rsv_iqid=0xf3348ced00002bfb&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=99669880_hao_pg&rsv_enter=1&rsv_dl=ib&rsv_sug3=2&rsv_sug1=1&rsv_sug7=001&rsv_n=2'
# url = 'https://blog.csdn.net/weixin_47834823/article/details/107939190'
url = 'https://blog.csdn.net/poweiliuxing/article/details/108582616'  #汪新 安装人工智能
url = 'https://blog.csdn.net/poweiliuxing/article/details/108596546'    #汪新 证件照换底色
url = 'https://blog.csdn.net/weixin_47834823/article/details/107893851' #我 安装人工智能
# url = 'https://blog.csdn.net/weixin_47834823/article/details/107939190' # 我 证件照换底色
url = 'https://blog.csdn.net/weixin_47834823/article/details/108517429' #pyton 内置基本函数
headers = [
        {"User-Agent": 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Mobile Safari/537.36'},
        {"User-Agent": 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'},
        {"User-Agent": 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'},
        {"User-Agent": 'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Mobile Safari/537.36'},
        {"User-Agent": 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Mobile Safari/537.36'},
        {"User-Agent": 'Mozilla/5.0 (BB10; Touch) AppleWebKit/537.10+ (KHTML, like Gecko) Version/10.0.9.2372 Mobile Safari/537.10+'},
        {"User-Agent": 'Mozilla/5.0 (Linux; U; Android 4.3; en-us; SM-N900T Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'},#Galaxy note3 待升级
        {"User-Agent": 'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LGMS323 Build/KOT49I.MS32310c) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.142 Mobile Safari/537.36'},#待升级
        {"User-Agent": 'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/14.14263'},
        # {"User-Agent": 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 7 Build/MOB30X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}, #开始
        {"User-Agent": 'Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 520)'},   #
        {"User-Agent": 'Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13'},# 11
        {"User-Agent": 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5'},
        {"User-Agent": 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Mobile Safari/537.36'},
        {"User-Agent": 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 10 Build/MOB31T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'},
        # {"User-Agent": 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; TencentTraveler 4.0; .NET CLR 2.0.50727)'},
        # {"User-Agent": 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)'},
        # {"User-Agent": 'Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999'},
        # {"User-Agent": 'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'},
        # {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'},
]
proxies_ip = [
        {'http': '61.135.185.160:80'},
        {'http': '61.135.185.152:80'},
        {'http': '61.135.185.118:80'},
        {'http': '222.74.202.227:9999'},
        {'http': '61.135.185.12:80'},
        {'http': '202.108.22.5:80'},
        {'http': '61.135.185.112:80'},
        {'http': '61.135.185.176:80'},
        {'http': '202.108.23.174:80'},
        {'http': '220.181.111.37:80'}
]
i = 0
while(True):
# for i in range(9):
    choice_agent = random.randint(0, 13)
    choice_ip = random.randint(0,9)
    print('本次随机提取的agent数字代号为：', headers[choice_agent], end='\t')
    sleep(1)
    data = requests.get(url, headers=headers[choice_agent], proxies=proxies_ip[choice_ip], timeout=5)
    soup = BeautifulSoup(data.text, 'html.parser')
    pretty_html = soup.prettify()
    lxml_html = etree.HTML(pretty_html)
    list_advertisement_url = lxml_html.xpath("//a[@href='http://chhs.0756tong.com/zhoushan/']")#//*[@id="content_views"]/p[2]/a     <a href="http://chhs.0756tong.com/zhoushan/">http://chhs.0756tong.com/zhoushan/</a>
    print(pretty_html)
    i = i+1
    print('-------------------------------------------------------------正在读取第'+str(i)+'次下载的文章-------------------------------------------------------------')
    sleep(59)
    print(pretty_html)
    print(data.status_code)
    


# choice_agent = random.randint(0, 8)
# header = headers[15]
# ip = proxies_ip[9]
# data = requests.get(url, headers=header, proxies={'http': '220.181.111.37:80'})
# soup = BeautifulSoup(data.text, 'html.parser')
# pretty_html = soup.prettify()
# lxml_html = etree.HTML(pretty_html)
# list_advertisement_url = lxml_html.xpath("//a[@href='http://chhs.0756tong.com/zhoushan/']")#//*[@id="content_views"]/p[2]/a     <a href="http://chhs.0756tong.com/zhoushan/">http://chhs.0756tong.com/zhoushan/</a>
# print(pretty_html)
# print(data.status_code)
# print(header)
# url = list_advertisement_url[0].text.strip()
# print(url)   #去处空格
# data = requests.get(url, headers=header, proxies={'http': 'http://123.125.114.107:80'})
# print(data)


# for i in range(100):
#         choice_agent = random.randint(0, 8)
#         header = headers[choice_agent]
#         ip = proxies_ip[9]
#         url = 'https://www.baidu.com/s?wd=http%3A%2F%2Fchhs.0756tong.com%2Fzhoushan%2F&rsv_spt=1&rsv_iqid=0x9043023500018fd4&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=78000241_5_hao_pg&rsv_enter=1&rsv_dl=tb&rsv_n=2&rsv_sug3=1&rsv_sug2=0&rsv_btype=i&inputT=1867&rsv_sug4=1868'
#         data = requests.get(url, headers=header, proxies=ip)
#         soup = BeautifulSoup(data.text, 'html.parser')
#         pretty_html = soup.prettify()
#         lxml_html = etree.HTML(pretty_html)
#         list_advertisement_url = lxml_html.xpath("//a[@href='http://chhs.0756tong.com/zhoushan/']")#//*[@id="content_views"]/p[2]/a     <a href="http://chhs.0756tong.com/zhoushan/">http://chhs.0756tong.com/zhoushan/</a>
#         print(pretty_html)
#         print(list_advertisement_url[0].text.strip())
#         print(data.status_code)
#         sleep(10)