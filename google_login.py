# from selenium import webdriver
from selenium.webdriver.common.by import By # for new way 2
from selenium.webdriver import Chrome, ChromeOptions
import time
import undetected_chromedriver as uc
import os
import json

def google_semi_auto_login():
    # driver = webdriver.Chrome() # 普通的Chrome Driver會被google anti-bot service 阻擋
    driver = uc.Chrome( ) # 換成 undetected-chrome driver 
    driver.get("https://accounts.google.com/InteractiveLogin/identifier?continue=https%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3Dgoogle%2Blogin%26rlz%3D1C1CHBF_zh-TWTW1057TW1057%26oq%3Dgoogle%2Blogi%26gs_lcrp%3DEgZjaHJvbWUqBwgAEAAYgAQyBwgAEAAYgAQyBwgBEAAYgAQyBggCEEUYOTIHCAMQABiABDIHCAQQABiABDIGCAUQRRg8MgYIBhBFGDwyBggHEEUYPKgCALACAA%26pf%3Dcs%26sourceid%3Dchrome%26ie%3DUTF-8%26pli%3D1&ec=GAZAAQ&hl=zh-TW&passive=true&ifkv=ASKXGp2BnUYGlXLq6SGO4m_7WlldRUloGm0x1jur6uZRavNPytsn57fce4TwA3RGniY8oRt_zh5PYQ&theme=glif&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    # step 1: google login
    time.sleep(3)
    driver.find_element(By.ID, "identifierId").send_keys(os.getenv('Gmail'))
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b']").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys(os.getenv('Gmail_pwd'))
    driver.find_element(By.XPATH, "//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b']").click()
    
    time.sleep(3)

    return driver

def start_chrome_with_profile(user_data_dir, profile_dir):
    user_data_dir_arg = f"--user-data-dir={user_data_dir}"
    profile_dir_arg = f"--profile-directory={profile_dir}"
    options = ChromeOptions()
    options.add_argument(user_data_dir_arg)
    options.add_argument(profile_dir_arg)
    driver = Chrome(options=options)
    return driver


if __name__ == '__main__':

    # driver = google_semi_auto_login()
    # driver.quit()
    # time.sleep(5)
    driver_2 = start_chrome_with_profile('chrome_profile', 'Default')
    time.sleep(10)
