# 我想要測試requests沒辦法第一時間取得google news首頁的內容
from bs4 import BeautifulSoup
import requests
import pprint

url = "https://news.google.com/home?hl=zh-TW&gl=TW&ceid=TW:zh-Hant"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

news_elements = soup.find_all('a', attrs={'class': 'WwrzSb'}) # 想要找到主頁面的焦點新聞
print(len(news_elements)) # 只能取得一開始的靜態網頁內容