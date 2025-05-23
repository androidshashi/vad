import torch
import json
from core.audio_utils import read_audio

# Load Silero VAD model
model, utils = torch.hub.load(
    repo_or_dir='snakers4/silero-vad',
    model='silero_vad',
    trust_repo=True
)

get_speech_timestamps = utils['get_speech_timestamps']

def run_vad_on_file(audio_path, output_path):
    wav = read_audio(audio_path)
    speech_timestamps = get_speech_timestamps(wav, model, sampling_rate=16000)

    with open(output_path, 'w') as f:
        json.dump(speech_timestamps, f, indent=4)
