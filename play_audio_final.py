from machine import I2S, Pin
import os

def play_audio(wav_file, sample_rate_in_hz=16000):
    # I2S Pin Configuration (adjust if needed)
    bck_pin = Pin(26)     # BCLK
    ws_pin = Pin(25)      # LRCLK
    sdout_pin = Pin(22)   # DIN to MAX98357A

    # I2S Setup
    audio_out = I2S(
        1,
        sck=bck_pin,
        ws=ws_pin,
        sd=sdout_pin,
        mode=I2S.TX,
        bits=16,
        format=I2S.MONO,
        rate=sample_rate_in_hz,
        ibuf=8000  # Larger buffer helps smoother playback
    )

    try:
        # Open WAV file
        wav = open(wav_file, "rb")
        wav.seek(44)  # Skip WAV header

        print("Playing audio...")

        buffer = bytearray(1024)
        mv = memoryview(buffer)

        while True:
            num_read = wav.readinto(mv)
            if num_read == 0:
                break

            num_written = 0
            while num_written < num_read:
                num_written += audio_out.write(mv[num_written:num_read])

        print("Playback finished.")

    except Exception as e:
        print("Playback error:", e)

    finally:
        wav.close()
        audio_out.deinit()

# Run standalone (not called by main.py)
if __name__ == "__main__":
    if "synthesized_audio.wav" in os.listdir():
        play_audio("synthesized_audio.wav", sample_rate_in_hz=16000)
    else:
        print("Audio file not found.")