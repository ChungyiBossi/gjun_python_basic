import speech_recognition as sr
from pydub import AudioSegment     # 載入 pydub 的 AudioSegment 模組


def semgment_audio(mp3_path, output_folder_path='.', duration_ms=3*1000, target_format='wav'):
    song = AudioSegment.from_file(mp3_path)    # 讀取 mp3 檔案
    for index in range(0, len(song), duration_ms): # 每30秒一個cut
        song[index: index + duration_ms].export(
            f"{output_folder_path}/{mp3_path}_{index}.wav",
            format=target_format
        ) 

def recognize_audio_file(wav_path, language='zh-TW'):
    r = sr.Recognizer()
    with sr.AudioFile(wav_path) as source:
        r.adjust_for_ambient_noise(source)
        audio = r.record(source)  # read the entire audio file
        try:
            text = r.recognize_google(audio, language)
            print("Google Speech Recognition thinks you said " + text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        
    return text if text else None
    
def recognize_voice_from_microphone(phrase_time_limit=0, language='zh-TW'):
    # 建立Recognizer物件
    r = sr.Recognizer()

    # 開啟麥克風並進行錄音
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        if phrase_time_limit:
            print(f"請開始說話...{phrase_time_limit} 秒後結束。")
            audio = r.listen(source, phrase_time_limit=phrase_time_limit)
        else:
            print(f"請開始說話直到你不想說話了。")
            audio = r.listen(source)
        # 使用Google語音辨識引擎將錄音轉換為文字
        try:
            text = r.recognize_google(audio, language)
            print("您說的是：" + text)
        except sr.UnknownValueError:
            print("無法辨識您的語音")
        except sr.RequestError as e:
            print("無法連線至Google語音辨識服務：{0}".format(e))
            
    return text if text else None
