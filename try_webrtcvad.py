
import webrtcvad
import wave
import scipy.io.wavfile as wf
import numpy as np

def load_wave(file_name):
    fp = wave.open(file_name, 'rb')
    try:
        assert fp.getnchannels() == 1, (
            '{0}: sound format is incorrect! Sound must be mono.'.format(
                file_name))
        assert fp.getsampwidth() == 2, (
            '{0}: sound format is incorrect! '
            'Sample width of sound must be 2 bytes.').format(file_name)
        assert fp.getframerate() in (8000, 16000, 32000), (
            '{0}: sound format is incorrect! '
            'Sampling frequency must be 8000 Hz, 16000 Hz or 32000 Hz.')
        sampling_frequency = fp.getframerate()
        sound_data = fp.readframes(fp.getnframes())
    finally:
        fp.close()
        del fp
    return sound_data, sampling_frequency

def read_wav(wave_file):
    rate, data = wf.read(wave_file)
    data = np.mean(data, axis=1, dtype=data.dtype) # convert to mono
    return data.tobytes(), rate


if __name__ == '__main__':
    # sound, sample_rate = read_wav('azure_30s.wav')
    # sound, sample_rate = read_wav('english.wav')
    sound, sample_rate = load_wave('leak-test.wav')
    frame_ms = 0.010
    frame_len = int(round(sample_rate* frame_ms))
    n = int(len(sound) / (2 * frame_len))

    vad = webrtcvad.Vad(3)
    print(frame_len, n, sample_rate)
    for frame_ind in range(n):
        find_voice = False
        slice_start = (frame_ind * 2 * frame_len)
        slice_end = ((frame_ind + 1) * 2 * frame_len)
        # print(slice_start, slice_end)
        if vad.is_speech(sound[slice_start:slice_end], sample_rate):
            find_voice = True
        print(f'find voice ({slice_start/1000}~{slice_end/1000}):', find_voice)
        