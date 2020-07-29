from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import requests
from requests.cookies import RequestsCookieJar
#启动谷歌浏览器
# chrome_options = webdriver.ChromeOptions() 
# chrome_options.add_argument('--no-sandbox')
# chrome = webdriver.Chrome(chrome_options=chrome_options)

options = Options()
# options.binary_location=r'C:/Users/Administrator/AppData/Local/Programs/Python/Python37/chromedriver.exe' 
options.add_experimental_option("debuggerAddress", "127.0.0.1:8081")

driver = webdriver.Chrome(options = options)
# driver.maximize_window()
# http://desktop.baibaiguanjia.com/#/
url_zuzhuang='http://3ganxiaoshuncom.wz.jgyljt.com/dede/index.php'
driver.get(url_zuzhuang)
cookie_dict=driver.get_cookies()
sess=requests.session()
jar=RequestsCookieJar()
for cookie in cookie_dict:
        jar.set(cookie['name'], cookie['value'])

data=sess.get(url_zuzhuang,cookies=jar)
print(data.content.decode('utf-8'))






























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