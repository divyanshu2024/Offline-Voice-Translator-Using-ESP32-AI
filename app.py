# Import all necessary libraries
import time
from speech_to_text import speech_to_text
from play_audio_final import play_audio
from record_audio_final import record_audio
from text_to_speech import translate_and_get_audio  # NEW IMPORT

# Main application logic with timing logs
def main():
    overall_start = time.ticks_ms()

    # Step 1: Record audio from the microphone
    try:
        print(" Recording audio...")
        t0 = time.ticks_ms()
        record_audio("Recording.wav")
        print(" Audio recording completed.")
        print(" Recording time:", time.ticks_diff(time.ticks_ms(), t0), "ms\n")
    except Exception as e:
        print(f" Error during audio recording: {e}")
        return

    # Step 2: Convert speech to text using Vosk
    try:
        print(" Sending audio to Vosk STT server...")
        t1 = time.ticks_ms()
        transcription = speech_to_text("Recording.wav")
        t1_end = time.ticks_ms()
        print(f"Transcription result:\n{transcription}\n")
        print("STT time:", time.ticks_diff(t1_end, t1), "ms\n")
    except Exception as e:
        print(f" Error during speech-to-text conversion: {e}")
        return

    # Step 3: Translate text and get audio from server
    if transcription:
        try:
            print(" Translating and fetching TTS...")
            t2 = time.ticks_ms()
            success = translate_and_get_audio(transcription, lang='te')  # or 'hi'
            t2_end = time.ticks_ms()
            if success:
                print(" Playing translated speech...")
                t3 = time.ticks_ms()
                play_audio("synthesized_audio.wav")
                t3_end = time.ticks_ms()
                print(" Audio playback time:", time.ticks_diff(t3_end, t3), "ms\n")
            else:
                print(" Translation or audio fetch failed.")
            print(" TTS + download time:", time.ticks_diff(t2_end, t2), "ms")
        except Exception as e:
            print(f" Error during translation or playback: {e}")

    total_time = time.ticks_diff(time.ticks_ms(), overall_start)
    print(f" Total pipeline time: {total_time} ms")

# Entry point
if __name__ == "__main__":
    main()