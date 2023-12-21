from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By # for new way 2
import time

# 1. 新建一個driver onject
driver = webdriver.Chrome() 
url = "https://news.google.com/home?hl=zh-TW&gl=TW&ceid=TW:zh-Hant"
driver.get(url)
time.sleep(2)
elements = driver.find_elements(By.XPATH, '//a[@class="WwrzSb"]') # //TAG_NAME[@ATTR_NAME=VALUE]
print(len(elements)) # 可以取得讀取完畢後的新聞

# for i, element in enumerate(elements):
#     print(i)
#     print(element.get_attribute('href'))
#     print()

# # 用AcitonChains操作網頁
# actions = ActionChains(driver) 
# for element in elements:
#     actions.move_to_element(element)
#     actions.scroll_to_element(element)
#     actions.pause(2)
# actions.perform()

time.sleep(5)