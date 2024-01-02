import speech_recognition as sr
from pydub import AudioSegment     # 載入 pydub 的 AudioSegment 模組


def semgment_audio(audio_path, duration_ms=3*1000, target_format='wav'):

    song = AudioSegment.from_file(audio_path)    # 讀取 mp3 檔案
    for index in range(0, len(song), duration_ms): # 每30秒一個cut
        song[index: index + duration_ms].export(f"{audio_path}_{index}.wav", format=target_format) 

if __name__ == '__main__':
    # semgment_audio('./River_South.mp3')
    r = sr.Recognizer()
    with sr.AudioFile('River_South.mp3_63000.wav') as source:
        r.adjust_for_ambient_noise(source)
        audio = r.record(source)  # read the entire audio file
        try:
            print("Google Speech Recognition thinks you said " + r.recognize_google(audio, language='zh-TW'))
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

