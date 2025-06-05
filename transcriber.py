from faster_whisper import WhisperModel

def transcribe_audio(audio_path, model_size="base.en"):
    print("[INFO] Transcribing audio...")
    model = WhisperModel(model_size, compute_type="int8")

    segments, _ = model.transcribe(audio_path)
    full_text = ""

    for segment in segments:
        print(f"[DEBUG] [{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")
        full_text += segment.text + " "

    return full_text.strip()
