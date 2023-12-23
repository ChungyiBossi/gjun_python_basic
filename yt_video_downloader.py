from selenium import webdriver
from selenium.webdriver.common.by import By
from pytube import YouTube
import time
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

def download_yt_video(yt_url, video_folder_path):
    yt = YouTube(yt_url)
    print(f'Download..., {yt.title}')

    # 可以用nltk去除特殊符號
    title = yt.title.replace("《", "").replace("》", "")
    try:
        yt.streams.filter().get_audio_only().download(
            output_path=f'{video_folder_path}',
            filename=f"{title}.mp3"
        )
        # 儲存為 mp3
        print('ok!')
    except Exception as e:
        print('Something wrong:', e)


def search_and_download_yt_video(driver, keyword):
    pattern = "+".join(keyword.split())

    driver.get(f"https://www.youtube.com/results?search_query={pattern}")
    time.sleep(10)

    href_list = list()
    video_elements = driver.find_elements(By.XPATH, '//a[@id="video-title"]')
    for element in video_elements:
        href = element.get_attribute('href')
        title = element.get_attribute('title')
        if href and title and keyword.lower() in title.lower():
            href_list.append(href)

    for href in href_list:
        download_yt_video(href, f'yt_video_folder/{keyword}')


if __name__ == '__main__':
    driver = webdriver.Chrome()
    search_and_download_yt_video(driver, 'Yoasobi')
