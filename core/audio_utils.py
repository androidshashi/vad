import torchaudio

def read_audio(file_path, sampling_rate=16000):
    wav, sr = torchaudio.load(file_path)
    if sr != sampling_rate:
        wav = torchaudio.functional.resample(wav, sr, sampling_rate)
    return wav[0]
