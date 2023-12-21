from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By # for new way 2
import time

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
# elem = driver.find_element_by_name("q") # 版本太舊已不能使用
# elem = driver.find_element("name", "q") # new way 1
elem = driver.find_element(By.NAME, "q") # new way 2
print(elem)
time.sleep(10)

elem.clear()
elem.send_keys("pycon") # 在搜尋欄打入"pycon"
time.sleep(10)

elem.send_keys(Keys.RETURN) # 搜尋
time.sleep(10)

assert "No results found." not in driver.page_source
driver.close() # 關閉web driver
time.sleep(10)