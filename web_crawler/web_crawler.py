from bs4 import BeautifulSoup
import requests
import pprint


def get_category_main_page_link(category_name):
    # 1. "Get" google news 網站
    r = requests.get(
        "https://news.google.com/home?hl=zh-TW&gl=TW&ceid=TW:zh-Hant")
    # 2. 取的回傳的DOM文字資料
    doc = r.text
    # 3. 把doc(DOM Tree)送給BeautifulSoup class, 做物件assign給soup這個變數
    soup = BeautifulSoup(doc, 'html.parser')
    # 4. 拿到國際新聞的頁面連結, 並取得內容
    # 4-1. 拿到所有element tag為"a"的DOM tree element, 並檢查是否有"href"和"aria-label"屬性
    elements_a = [
        element for element in soup.find_all('a')
        if element.get("href") and element.get("aria-label")
    ]
    # 4-2. 取出aria-label == category 的DOM Tree element
    category_news_href = ""
    for element in elements_a:
        if element.get("aria-label") == category_name:
            category_news_href = \
                'https://news.google.com' + element.get("href")[1:]
            break
    return category_news_href


def get_category_news_blocks(category_main_page_link):

    # 4-3. 去request 類別的主頁面
    page_text = requests.get(category_main_page_link).text
    soup = BeautifulSoup(page_text, 'html.parser')

    # 5. 分塊拿到類別新聞: element tag=c-wiz, class=PO9Zff Ccj79 kUVvS
    block_elements = soup.find_all(
        'c-wiz', {'class': 'PO9Zff Ccj79 kUVvS'})

    return block_elements


def get_google_news(category_name):
    news_href = get_category_main_page_link(category_name)
    news_blocks = get_category_news_blocks(news_href)
    # 6. 找到每個block內, 所有的新聞標題與超連結
    block_news = dict()
    for block_index, block in enumerate(news_blocks):
        titles = list()
        # 6.1. 找標題
        for title_element in block.find_all('a', {'class': 'gPFEn'}):
            titles.append(title_element.string)

        # 6.2. 找連結
        links = list()
        for link_element in block.find_all('a', {'class': 'gPFEn'}):
            links.append('https://news.google.com' +
                         link_element.get("href")[1:])

        # 6.3. 找媒體商
        media = list()
        for media_element in block.find_all('div', {'class': 'vr1PYe'}):
            media.append(media_element.text)

        # 6.4 找時間
        timestamp = list()
        for time_element in block.find_all("time", {'class': "hvbAAd"}):
            timestamp.append(time_element.get('datetime'))

        result = list(zip(titles, links, media, timestamp))
        if result:
            block_news[block_index] = result

    return block_news


if __name__ == '__main__':

    news = get_google_news(category_name="娛樂")
    pprint.pprint(news)
