from flask import Flask, jsonify, render_template, request
from robottools import RobotTools

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    ip = request.form['ip']
    port = request.form['port']
    text = request.form['text']

    rt = RobotTools(ip, int(port))

    if '\n' in text:
        text = text.replace('\r\n', '').replace('\n', '')

    d = rt.say_text(text)
    m = rt.make_beat_motion(d)
    rt.play_motion(m)

    return jsonify({'message': f'入力されたテキスト: {text}'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
