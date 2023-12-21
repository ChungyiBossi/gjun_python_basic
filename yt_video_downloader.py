from selenium import webdriver
from selenium.webdriver.common.by import By
from pytube import YouTube
import time
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

def download_yt_video(yt_url, video_folder_path):
    yt = YouTube(yt_url)
    print(f'Download..., {yt.title}')
    yt.streams.filter().get_audio_only().download(output_path=f'{video_folder_path}', filename=f"{yt.title}.mp3")
    # 儲存為 mp3
    print('ok!')


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/results?search_query=jay+chou")
    time.sleep(10)

    href_list = list()
    video_elements = driver.find_elements(By.XPATH, '//a[@id="video-title"]')
    for element in video_elements:
        href = element.get_attribute('href')
        title = element.get_attribute('title')
        if href and title and "周杰倫 Jay Chou" in title:
            href_list.append(href)
            print(title, href)
            print()

    for href in href_list:
        download_yt_video(href, 'yt_video_folder')
