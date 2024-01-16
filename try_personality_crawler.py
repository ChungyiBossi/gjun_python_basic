import pandas as pd
import time
import random
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# 定義在外面，保持相同的狀態
authors_set = set()
all_posts_data = []


def crawl_thread(thread_url):
    # use beautifulsoup instead
    r = requests.get(thread_url)
    content = r.content
    thread_posts_soup = BeautifulSoup(content, 'html.parser')
    post_content_element = thread_posts_soup.find('div', class_='bbWrapper')
    post_content = post_content_element.text.strip() if post_content_element else ''

    # 獲取作者名稱
    author_element = thread_posts_soup.find(
        'a', class_='MessageCard__user-info__name')
    author_name = author_element.text if author_element else ''

    # 獲取貼文標題
    thread_title_element = thread_posts_soup.find(
        'h1', class_='MessageCard__thread-title')
    thread_title = thread_title_element.text.strip() if thread_title_element else ''

    print(f"Processing post from {author_name} ({thread_url})....finished!")

    return {
        'Author': author_name,
        'Thread_Title': thread_title,  # 加入貼文標題
        'Content': post_content,
        'Thread_URL': thread_url
    }


def crawl_istp_forum(base_url, author_limit=500, output_path="istp_posts_data.csv"):
    # 初始化Chrome Driver
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'  # 希望加快讀取速度，或是是否能用BS4取代Selenium?
    driver = webdriver.Chrome(
        options=options
    )
    # 初始頁面
    url = base_url
    driver.get(url)
    print('Get forum web page.')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'structItem-title'))
    )

    # 找到qid為"page-nav-other-page"的元素
    # page_nav_element = soup.select_one('[qid="page-nav-other-page"]')
    page_nav_element = driver.find_element(
        By.XPATH, '//*[@qid="page-nav-other-page"]')

    # 從中獲取頁數
    total_pages = int(page_nav_element.text)
    print(total_pages)

    for page in range(1, total_pages + 1):
        # 動態生成網址
        if page == 1:
            url = base_url
        else:
            url = f"{base_url}page-{page}?sorting=latest-activity"

        print(f'Page {page} start. url:{url}')
        driver.get(url)
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, 'structItem-title'))
        )

        # soup = BeautifulSoup(driver.page_source, 'html.parser')
        # thread_links = soup.find_all('a', class_='thread-title--gtm')
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, '//a[@class=" thread-title--gtm"]'))
        )
        thread_links_elements = driver.find_elements(
            By.XPATH, '//a[@class=" thread-title--gtm"]')

        # To solve bug: "Message: stale element reference: stale element not found"
        # need to store thread links to prevent bug above
        links = list()
        for elements in thread_links_elements:
            link = elements.get_attribute('href')
            links.append(link)

        print(f'{len(links)} threads find')
        for i, thread_url in enumerate(links):
            try:
                # random sleep
                time.sleep(random.randint(1, 5))
                # get thread content
                post_content = crawl_thread(thread_url)
                # 檢查是否已經爬取過該作者的貼文
                if post_content['Author'] not in authors_set:
                    # 加入到作者列表
                    authors_set.add(post_content['Author'])
                    # 處理該作者的貼文內容
                    all_posts_data.append(post_content)

                # 如果已經達到指定作者數目，則退出迴圈
                if len(authors_set) >= author_limit:
                    break
            except TimeoutException:
                print(
                    f"TimeoutException: Timed out on thread {i + 1}. Skipping...")
                pass
            time.sleep(random.randint(1, 5))

        # 如果已經達到指定作者數目，則退出迴圈
        if len(authors_set) >= author_limit:
            break
        # 模擬滾動以加載更多帖子，這部分可視情況選擇是否需要
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

        # 每次迴圈結束都將資料保存到 CSV 檔案
        df_posts = pd.DataFrame(all_posts_data)
        df_posts.to_csv(output_path, index=False)
        print(f"Saved data to {output_path}")

    driver.quit()

    return all_posts_data



if __name__ == '__main__':
    # 設定論壇基本網址
    base_forum_url = "https://www.personalitycafe.com/forums/istp-forum-the-mechanics.9/"

    # 設定要爬取的作者數目
    author_limit = 500

    # 設定輸出檔案的路徑
    output_csv_path = "data_personality/istp_data.csv"

    # 爬取資料
    all_posts_data = crawl_istp_forum(
        base_forum_url, author_limit, output_path=output_csv_path)

    # 將所有的資料轉換成 DataFrame
    df_all_posts = pd.DataFrame(all_posts_data)

    # 檢查爬取到的作者數量是否足夠
    if len(authors_set) < author_limit:
        print(
            f"Warning: Only crawled {len(authors_set)} unique authors, which is less than the required {author_limit}. The data may not be sufficient.")