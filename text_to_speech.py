# text_to_speech.py

import urequests

def translate_and_get_audio(text, lang='te'):
    url = "http://192.168.219.54:5001/translate_speak"
    headers = {'Content-Type': 'application/json'}
    payload = {'text': text, 'lang': lang}

    try:
        # POST request with stream=True (urequests in MicroPython doesn't officially support this param,
        # but raw stream can still be used)
        response = urequests.post(url, json=payload)
        if response.status_code == 200:
            # Open file for writing binary audio data
            with open("synthesized_audio.wav", "wb") as f:
                # Read response in small chunks to avoid memory overload
                while True:
                    chunk = response.raw.read(512)  # read 512 bytes at a time
                    if not chunk:
                        break
                    f.write(chunk)
            response.close()
            return True
        else:
            print(f"Server error: {response.status_code}")
            response.close()
            return False
    except Exception as e:
        print(f"Error fetching audio: {e}")
        return False