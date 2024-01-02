import speech_recognition as sr

# 建立Recognizer物件
r = sr.Recognizer()

# 開啟麥克風並進行錄音
with sr.Microphone() as source:
    print("請開始說話...")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(
        source
        # phrase_time_limit=10
    )

# 使用Google語音辨識引擎將錄音轉換為文字
try:
    text = r.recognize_google(audio, language='zh-TW')
    print("您說的是：" + text)
except sr.UnknownValueError:
    print("無法辨識您的語音")
except sr.RequestError as e:
    print("無法連線至Google語音辨識服務：{0}".format(e))