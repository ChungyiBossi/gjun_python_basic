import mido
import librosa
import time
# from midi2audio import FluidSynth


def save_chroma_as_midi(chroma, midi_file_path):
    midi_file = mido.MidiFile()

    # 创建一个 MidiTrack 对象
    track = mido.MidiTrack()
    midi_file.tracks.append(track)

    # ticks_per_beat = 2  # 可根据需要调整
    # print("ticks per beat: ", ticks_per_beat)

    # 将 Chromagram 转换为 MIDI 符号并添加到 MidiTrack 中

    for time_step in range(chroma.shape[1]):
        
        max_arg = chroma[:, time_step].argmax()
        inter = 127/12
        # note =  round(max_arg * inter)  # 計算線性組合強度(?)
        note = 60
        # print('Note: ', note, max_arg)
        if note > 0:
            # 添加 Note On 事件到 MidiTrack
            note_on = mido.Message('note_on', note=note)
            track.append(note_on)
            track.append(mido.Message('note_off', note=note, velocity=0, 
                                    #   time=ticks_per_beat
            ))
    print("track: ", len(track))
    # 保存 MidiFile 为 MIDI 文件
    midi_file.save(midi_file_path)

if __name__ == '__main__':

    # 加载音频文件
    # https://stackoverflow.com/questions/61986490/what-does-librosa-load-return
    amplitudes, sample_rate = librosa.load(
        "./audio_files/azure_30s.wav",
        # sr=None # default sample rate = 22050
    )

    print("amplitudes: ", amplitudes.shape, ', sample rate: ',sample_rate)

    # 得到chroma
    chroma = librosa.feature.chroma_stft(y=amplitudes, sr=sample_rate)
    print('# of chroma: ', chroma.shape)
    print('audio length: ', amplitudes.shape[0]/sample_rate)


    # 指定保存的 MIDI 文件路径
    midi_file_path = './input.mid'  # 替换为你实际想要保存 MIDI 文件的路径

    # # 保存 Chromagram 为 MIDI 文件
    # save_chroma_as_midi(chroma, midi_file_path)

    # # 使用FluidSynth将MIDI文件转换为WAV格式
    sound_font_path = './MuseScore_General_Full.sf2'
    # fs = FluidSynth(sound_font=sound_font_path, sample_rate=sample_rate)

    # # 轉換成audio並儲存
    # fs.midi_to_audio(midi_file_path, './output.wav')

    # # 加载并播放WAV文件
    # audio = AudioSegment.from_wav('output.wav')

    import fluidsynth

    # 创建 FluidSynth 合成器
    fs = fluidsynth.Synth()

    # 设置声音字体文件路径（SoundFont 文件）
    fs.start(driver="alsa")  # 根据需要设置音频驱动

    # 载入声音字体
    fs.sfload(sound_font_path)

    # 设置合成器参数
    fs.program_select(0, fs.sfload(sound_font_path), 0, 0)

    # 读取 MIDI 文件并播放
    fs.midifile_load(midi_file_path)

    # 播放 MIDI 文件
    fs.play()

    # 等待 MIDI 播放完毕
    while fs.active():
        pass

    # 关闭合成器
    fs.delete()
