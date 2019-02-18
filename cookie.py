from selenium import webdriver
import time
chrome_options = webdriver.ChromeOptions()
browser = webdriver.Chrome(options=chrome_options)

browser.get("https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fwww.taobao.com%2F")
buttom=browser.find_element_by_id('J_Quick2Static')
buttom.click()
input=browser.find_element_by_id('TPL_username_1')
input.send_keys('15950092787')
time.sleep(1)
input1=browser.find_element_by_id('TPL_password_1')
input1.send_keys('dxx2301116380')
time.sleep(1)
buttom1=browser.find_element_by_id('J_SubmitStatic')
buttom1.click()
time.sleep(5)
cookie = browser.get_cookies()
print(cookie)