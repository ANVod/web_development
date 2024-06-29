from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f"<h1>Сейчас в Москве</h1><p>{current_time}</p>"


if __name__ == '__main__':
    app.run(debug=True)