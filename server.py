from flask import Flask, request, jsonify
import wave
import os
from vosk import Model, KaldiRecognizer

app = Flask(__name__)
TEMP_AUDIO = "received.wav"

model = Model("model")  # Your Vosk model path
recognizer = KaldiRecognizer(model, 16000)

# Temporary store for audio data
buffer = bytearray()

@app.route('/stt', methods=['POST'])
def stt():
    global buffer

    x_complete = request.headers.get('X-Complete', 'false')

    # Collect incoming audio
    if x_complete == 'false':
        buffer.extend(request.data)
        return "Chunk received", 200

    # Final chunk received — process audio
    elif x_complete == 'true':
        print("Final chunk received. Processing audio...")

        # Save audio to temp WAV file
        with wave.open(TEMP_AUDIO, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(16000)
            wf.writeframes(buffer)

        buffer = bytearray()

        # Perform STT
        with wave.open(TEMP_AUDIO, 'rb') as wf:
            recognizer = KaldiRecognizer(model, wf.getframerate())
            result_text = ""
            while True:
                data = wf.readframes(4000)
                if len(data) == 0:
                    break
                if recognizer.AcceptWaveform(data):
                    pass
            result = recognizer.FinalResult()

        os.remove(TEMP_AUDIO)
        return jsonify({"transcript": result})

    return "Invalid request", 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)