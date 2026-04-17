from flask import Flask, render_template, request, send_file
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def convert():
    text = request.form.get('text')

    if not text:
        return render_template('index.html', error="Please enter text")

    tts = gTTS(text=text, lang='pa')
    
    if not os.path.exists('static'):
        os.makedirs('static')

    filename = "static/output.mp3"
    tts.save(filename)

    return render_template('index.html', audio=filename, text=text)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
