from bs4 import BeautifulSoup
import requests

# 1. 請求google news網頁內容, 使用 GET 方法 (Restful API)
response = requests.get("https://news.google.com/home?hl=zh-TW&gl=TW&ceid=TW:zh-Hant")
# print(response.content[:500], len(response.content))

# 2. 把網頁內容丟給漂亮湯做Parse
soup = BeautifulSoup(response.content, 'html.parser')
# print([child.name for child in soup.html.body.children])

# 3. 找到特定的tag, 並存成dictionary
import pprint 
a_elements = soup.find_all('a', attrs={'class':'brSCsc'}) # 意思是找到class為'brSCsc'的a標籤
topic_links = dict()
for element in a_elements:
    if 'href' in element.attrs:
        topic_links[element['aria-label']] = 'https://news.google.com/' + element['href'][2:]
        # print(element['aria-label'], 'https://news.google.com/' + element['href'][2:])
        # print()
# pprint.pprint(topic_links)


# 4. 重複1~3連接到體育新聞
response = requests.get(topic_links['體育'])
soup = BeautifulSoup(response.content, 'html.parser')
article_elements = soup.find_all('article')
news = list()
for article in article_elements:
    title_element = article.find_all('a', attrs={'class':'gPFEn'})
    if title_element: # 有找到才處理
        title_element = title_element[0] 
        news.append({
            'href': 'https://news.google.com/' + title_element['href'][2:],
            'title': title_element.string
        })
    # print(article.div.a['href'])
    # print()
print(len(news))
pprint.pprint(news[0])