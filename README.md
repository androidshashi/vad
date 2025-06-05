
# Voice Activity Detection (VAD) Project

## Overview
This project implements a modular Voice Activity Detection (VAD) system using `webrtcvad` and `faster-whisper` for speech transcription. It records audio from the microphone, detects speech segments with silence-based stopping logic, and transcribes the recorded audio using the Whisper model.

The project is designed to be easily integrated into larger applications.

## Features
- Real-time audio recording with VAD-based speech detection.
- Automatic stop after detecting continuous silence.
- Transcription of recorded audio using `faster-whisper` WhisperModel.
- Modular structure for easy integration and reuse.

## Requirements
- Python 3.7+
- `pyaudio`
- `webrtcvad`
- `faster-whisper`
- `numpy`

## Installation

```bash
pip install pyaudio webrtcvad faster-whisper numpy
```

## Usage

### Basic Example

```python
from vad_module import VoiceActivityDetector, WhisperTranscriber

if __name__ == "__main__":
    vad = VoiceActivityDetector()
    filename = vad.record_audio()
    transcriber = WhisperTranscriber()
    transcription = transcriber.transcribe_audio(filename)
    print("\nFinal Transcription:\n", transcription)
```

## Module Details

### `vad_module.py`

- `VoiceActivityDetector`
  - `record_audio(filename=None)`: Records audio from the microphone and saves to `filename`.

- `WhisperTranscriber`
  - `transcribe_audio(audio_path)`: Transcribes given audio file and returns text.

## Configuration

You can customize parameters such as:
- Sample rate
- Frame duration
- Silence timeout duration

by modifying the class initialization parameters.

## Troubleshooting

- If you get warnings from `faster-whisper`, consider updating dependencies or using a different compute type.
- For audio input errors, ensure your microphone and `pyaudio` installation are working correctly.

## License

MIT License

---

This VAD module is designed for easy integration into AI assistant projects.
