import threading
import requests 
from selenium import webdriver
from bs4 import BeautifulSoup
import re
from lxml import etree
from threading import Thread, Lock, enumerate
from time import sleep
import random
from showtime import runningtime
from requests.cookies import RequestsCookieJar
import xlrd
import xlwt

excle_path = r'C:/Users/Administrator/Desktop/test.xlsx'  #路径
workbook = xlrd.open_workbook(excle_path)     #打开excle表
sheet = workbook.sheet_by_name('sheet1')    #打开sheet表单页
domain_names = []
keywords = []
for i in range(30):
    keywords.append(sheet.cell(i, 0).value)
    domain_names.append(sheet.cell(i, 1))
# 进入浏览器设置
options = webdriver.ChromeOptions()
options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Mobile Safari/537.36"')


google_driver = webdriver.Chrome(chrome_options=options) #启动谷歌
google_driver.maximize_window()  # 最大化窗口

def download_sm(url, sess, jar, i, keyword):
    print('--------------------------正在下载第' + str(i) + '篇"'+keyword+'"的URL域名--------------------------')
    header = {
        "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Mobile Safari/537.36'
    }
    # html = requests.get(url, headers=header).content.decode('utf-8')  # 下载并解码
    data=sess.get(url,cookies=jar, headers=header).content.decode('utf-8')
    soup = BeautifulSoup(data, 'html.parser')
    pretty_html = soup.prettify()
    return pretty_html


def data_clean(pretty_html, num):
    # print(pretty_html)    #输出源码
    lxml_html = etree.HTML(pretty_html)
    list_advertisement_url = lxml_html.xpath("//div[@class='other']")
    # list_advertisement = lxml_html.xpath("//div[@class='other']//span")

    i = 0
    for value in list_advertisement_url:
        value = value.text.strip()
        i = i+1
        if(value == domain_names[num-1].value):
             print(value+"\t序号："+str(i)+"\t\t"+domain_names[num-1].value)
        else:
            print(value+"\t序号："+str(i))
        
@runningtime
def start():
    num = 0
    for keyword in keywords:
        num = num+1
        url = 'https://m.sm.cn/s?q='+keyword+'&by=submit&from=smor&tomode=center&safe=1'
        google_driver.get(url)
        sleep(4)
        cookie_dict=google_driver.get_cookies()
        sess=requests.session()
        jar=RequestsCookieJar()
        for cookie in cookie_dict:
                jar.set(cookie['name'], cookie['value'])

        pretty_html = download_sm(url, sess, jar, num, keyword)
        # print(pretty_html)
        data_clean(pretty_html, num)

if __name__ == "__main__":
    start()