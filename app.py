from flask import Flask, render_template, request
from gtts import gTTS
import os
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    title = request.form.get('title', '')
    text = request.form.get('text', '')
    lang = request.form.get('lang', 'pa')
    speed = request.form.get('speed', 'normal')

    # empty check
    if text.strip() == "":
        return render_template('index.html', error="Please enter story text")

    # combine title + text
    final_text = f"{title}. {text}"

    # create static folder
    if not os.path.exists('static'):
        os.makedirs('static')

    # unique filename
    filename = f"static/story_{int(time.time())}.mp3"

    # speed control
    slow = True if speed == "slow" else False

    # generate audio
    tts = gTTS(text=final_text, lang=lang, slow=slow)
    tts.save(filename)

    return render_template('index.html', audio_file=filename, text=text, title=title)

if __name__ == '__main__':
    app.run(debug=True)