import wave
import webrtcvad
import pyaudio
from config import *
from utils import get_timestamped_filename

def record_audio(filename=None):
    vad = webrtcvad.Vad(3)
    pa = pyaudio.PyAudio()
    stream = pa.open(format=FORMAT,
                     channels=CHANNELS,
                     rate=SAMPLE_RATE,
                     input=True,
                     frames_per_buffer=FRAME_SIZE)

    frames = []
    silent_chunks = 0

    if not filename:
        filename = get_timestamped_filename()

    print("[INFO] Listening... Start speaking.")

    try:
        while True:
            frame = stream.read(FRAME_SIZE, exception_on_overflow=False)
            is_speech = vad.is_speech(frame, SAMPLE_RATE)
            print(f"[DEBUG] is_speech={is_speech}, silent_chunks={silent_chunks}")

            frames.append(frame)

            if is_speech:
                silent_chunks = 0
            else:
                silent_chunks += 1

            if silent_chunks > MAX_SILENT_FRAMES:
                print("[INFO] Silence detected. Stopping recording.")
                break

    except KeyboardInterrupt:
        print("[WARN] Interrupted by user.")

    stream.stop_stream()
    stream.close()
    pa.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(pa.get_sample_size(FORMAT))
    wf.setframerate(SAMPLE_RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    return filename
