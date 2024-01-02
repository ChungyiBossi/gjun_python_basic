from web_crawler.google_login import google_semi_auto_login
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import os, time, json

def login_to_chatgpt(driver):
    # step 3: login openai
    driver.get('https://chat.openai.com/')
    driver.find_element(By.XPATH, '//button[@data-testid="login-button"]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//button[@class="cf8ab1d76 ca5439885 c90865442"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//div[@class="lCoei YZVTmd SmR8"]').click()
    time.sleep(5)
    return driver

def continuous_chat_wtih_chatgpt(driver):

    # step 4: input text
    conversation = list()
    while True:
        input_text = input("What you want to say?")
        if input_text == 'quit':
            break
        content = chat_with_chatgpt(driver, input_text)
        conversation.append({
            'user': input_text,
            'system': content
        })

    return driver, conversation

def chat_with_chatgpt(dirver, input_text):
    textarea_element = driver.find_element(By.ID, 'prompt-textarea')
    textarea_element.send_keys(input_text)
    textarea_element.send_keys(Keys.RETURN)
    time.sleep(10)
    last_response = driver.find_elements(
        By.XPATH,
        '//div[@class="markdown prose w-full break-words dark:prose-invert light"]'
    )[-1]
    response_text_elements = last_response.find_elements(By.TAG_NAME, 'p')
    content = list()
    for p in response_text_elements:
        content.append(p.text)
    content = "".join(content)
    return content

if __name__ == '__main__':
    driver = google_semi_auto_login(os.getenv('Gmail'), os.getenv('Gmail_pwd'))
    driver = login_to_chatgpt(driver)
    driver, conversation = continuous_chat_wtih_chatgpt(driver)
    with open(f'{time.time()}.json', 'w') as output:
        conversation = json.dumps(conversation)
        output.write(conversation)

    driver.close()