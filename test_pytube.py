import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

from pytube import YouTube
yt = YouTube('https://www.youtube.com/watch?v=R93ce4FZGbc')
print('download...')
yt.streams.filter().get_audio_only().download()
# 儲存為 mp3
print('ok!')