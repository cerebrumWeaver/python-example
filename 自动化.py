from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import requests
from requests.cookies import RequestsCookieJar
from lxml import etree
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

#   chrome.exe --remote-debugging-port=12306 --user-data-dir="C:\Users\Administrator\Desktop\Google"
#   www.nbbaibai.com

#启动谷歌浏览器
# chrome_options = webdriver.ChromeOptions() 
# chrome_options.add_argument('--no-sandbox')
# chrome = webdriver.Chrome(chrome_options=chrome_options)

options = Options()
# options.binary_location=r'C:/Users/Administrator/AppData/Local/Programs/Python/Python37/chromedriver.exe' 
options.add_experimental_option("debuggerAddress", "127.0.0.1:12306")

driver = webdriver.Chrome(options = options)
# driver.maximize_window()
# http://desktop.baibaiguanjia.com/#/<div class="fllct"><a href="catalog_main.php" target="main">网站栏目管理</a></div>
url_zuzhuang='http://wwwnbbaibaicom.wz2.jgyljt.com/dede/index.php'
driver.get(url_zuzhuang)
driver.switch_to.frame('menufra')  #需先跳转到iframe框架
# driver.find_element_by_xpath("//div[@class='left']//div[@class='fllct']//a").click()
# driver.find_element_by_link_text('catalog_main.php').click()

aElements = driver.find_elements_by_tag_name("a")

for name in aElements:
    # print(name)
    if(name.get_attribute("href") is not None and "catalog_main.php" in name.get_attribute("href")):
        # print("IM IN HUR")
        name.click()
        break

cookie_dict=driver.get_cookies()
sess=requests.session()
jar=RequestsCookieJar()
for cookie in cookie_dict:
        jar.set(cookie['name'], cookie['value'])

data=sess.get(url_zuzhuang,cookies=jar)
data=data.content.decode('utf-8')
# print(data)
lxml_html = etree.HTML(data)

# print(lxml_html.xpath("//div[@class='left']//div[@class='fllct']"))
# <a href="catalog_do.php?cid=17&amp;dopost=listArchives">症状[ID:17]</a>

driver.switch_to.default_content()
driver.switch_to.frame('main')  #需先跳转到iframe框架
aElements = driver.find_elements_by_tag_name("a")
for name in aElements:
    if(name.get_attribute("href") is not None and "catalog_do.php?cid=17&dopost=listArchives" in name.get_attribute("href")):
        name.click()
        break

#   添加文章 按钮
input_Elements = driver.find_elements_by_tag_name("input")
for name in input_Elements:
    if(name.get_attribute("type") is not None and "button" in name.get_attribute("type")):
        name.click()
        break

#  文章标题 文本框
title=driver.find_element_by_id('title')
title.send_keys('文章标题')


#  自定义属性 复选框
custom_properties=driver.find_element_by_id('flagsp')
custom_properties.click()

#  TAG标签 文本框
tag=driver.find_element_by_id('tags')
tag.send_keys('TAG标签')

#  文章来源 文本框
source=driver.find_element_by_id('source')
source.send_keys('未知')

#  作者 文本框
writer=driver.find_element_by_id('writer')
writer.send_keys('姓名')

#  文本内容 文本域
#cke_contents_body > iframe
no_properties_iframe = driver.find_element_by_css_selector('#cke_contents_body > iframe')
driver.switch_to.frame(no_properties_iframe)  #需先跳转到iframe框架
textarea = driver.find_element_by_class_name('cke_show_borders')
# textarea.send_keys('文本内容')
# send_keys(Keys.CONTROL,'a')  # 全选(Ctrl+A)
# send_keys(Keys.CONTROL,'c')  # 复制(Ctrl+C)
# send_keys(Keys.CONTROL,'x')  # 剪切(Ctrl+X)
# send_keys(Keys.CONTROL,'v')  # 粘贴(Ctrl+V)

# 1.实例化ActionChains类
ac = ActionChains(driver)
ac.move_to_element(textarea).perform()
textarea.send_keys(Keys.CONTROL,'v')
# ac.move_to_element_with_offset
# textarea.
# body > p:nth-child(1)
# body > p:nth-child(3)
# p1 = driver.find_element_by_css_selector('body > p:nth-child(1)')
# print(p1.get_text())
# cke_63
textarea.send_keys(Keys.CONTROL,'a')
driver.switch_to.default_content()
driver.switch_to.frame('main')
a_color=driver.find_element_by_id('cke_63')
a_color.click()
a = driver.switch_to_active_element
#    if(name.get_attribute("type") is not None and "button" in name.get_attribute("type")):
# s = Select(a)
# s.select_by_value('红色')
# a.click()








# html=requests.get(url_zuzhuang, headers=header).content.decode('utf-8')
# print(html)
    #driver.get("https://www.baidu.com/")
    #回退上一页
    # 
    # sleep(2)
    # driver.back()

    #回到下一页

    # driver.forward()

    #刷新

    # driver.refresh()

    #获取标题

    # print("标题："+driver.title)

    #获取网址
    # print("网址："+driver.current_url)

    #窗口的句柄

    # print("窗口句柄："+driver.current_window_handle)

    #结束会话

# driver.close() #关闭浏览器的一个页签

# driver.quit() #关闭浏览器，退出当前会话