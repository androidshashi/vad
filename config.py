import pyaudio

# Audio Configuration Constants
SAMPLE_RATE = 16000
CHANNELS = 1
FORMAT = pyaudio.paInt16
FRAME_DURATION = 30  # ms
FRAME_SIZE = int(SAMPLE_RATE * FRAME_DURATION / 1000)
MAX_SILENT_FRAMES = int(2000 / FRAME_DURATION)  # 2 seconds
