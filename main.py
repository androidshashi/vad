from core.vad_processor import run_vad_on_file

if __name__ == "__main__":
    audio_path = "data/sample.wav"
    output_path = "output/vad_segments.json"

    run_vad_on_file(audio_path, output_path)
    print(f"VAD processing complete. Results saved to {output_path}")
