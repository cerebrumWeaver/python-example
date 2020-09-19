from selenium import webdriver
from time import sleep
#启动谷歌浏览器
driver=webdriver.Chrome()
# driver=webdriver.Firefox(executable_path=r'c://ProgramFiles//seleniem_driver//geckodriver.exe')
# driver=webdriver.Edge()
#访问一个网页
driver.get("https://github.com/login")

# 窗口最大化
# driver.maximize_window()
sleep(2)
username=driver.find_element_by_id('login_field')
password=driver.find_element_by_id('password')
btn=driver.find_element_by_name('commit')
username.send_keys('cerebrumWeaver')
password.send_keys('678567okytfytm')
btn.click()
sleep(2)

# #回退上一页
# driver.back()

#回到下一页

driver.forward()

#刷新

# driver.refresh()

#获取标题

print(driver.title)

#获取网址
print(driver.current_url)

#窗口的句柄

print(driver.current_window_handle)

#结束会话

driver.close() #关闭浏览器的一个页签

driver.quit() #关闭浏览器，退出当前会话