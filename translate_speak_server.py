from flask import Flask, request, jsonify, send_file
from gtts import gTTS
from deep_translator import GoogleTranslator
import subprocess

app = Flask(__name__)

@app.route('/translate_speak', methods=['POST'])
def translate_and_speak():
    data = request.get_json()
    text = data.get("text", "")
    lang = data.get("lang", "hi")  # Default: Hindi

    if not text:
        return jsonify({"error": "No text provided"}), 400

    try:
        # 1. Translate the input
        translated = GoogleTranslator(source='auto', target=lang).translate(text)

        # 2. Generate MP3 using gTTS
        mp3_path = "temp.mp3"
        tts = gTTS(text=translated, lang=lang)
        tts.save(mp3_path)

        # 3. Convert MP3 → WAV (Mono, 22050 Hz, 16-bit PCM)
        wav_path = "translated_audio.wav"
        subprocess.run([
            "ffmpeg", "-y", "-i", mp3_path,
            "-ar", "16000", "-ac", "1", "-sample_fmt", "s16",
            wav_path
        ], check=True)

        # 4. Send the final WAV file
        return send_file(wav_path, mimetype="audio/wav")

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)