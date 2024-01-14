
from midi2audio import FluidSynth

def midi_to_wav(midi_file_path, sound_font_path='./MuseScore_General_Full.sf2'):
    # 使用FluidSynth将MIDI文件转换为WAV格式
    
    fs = FluidSynth(sound_font=sound_font_path)

    # 轉換成audio並儲存
    output_file_path = midi_file_path.replace('.mid', '.wav')
    fs.midi_to_audio(midi_file_path, output_file_path)

if __name__ == '__main__':


    # # 指定保存的 MIDI 文件路径
    midi_file_path = './River_South.mid'

    midi_to_wav(midi_file_path)

