from recorder import record_audio
from transcriber import transcribe_audio

if __name__ == "__main__":
    audio_file = record_audio()
    transcription = transcribe_audio(audio_file)
    print("\n[RESULT] Final Transcription:\n", transcription)
