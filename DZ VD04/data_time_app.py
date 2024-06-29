from flask import Flask
from datetime import datetime

app = Flask(__name__)#создание приложения


@app.route('/')#главная страница
def home():#функция
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')#текущее время
    return f"<h1>Сейчас в Москве</h1><p>{current_time}</p>"#вывод текущего времени


if __name__ == '__main__':#запуск приложения
    app.run(debug=True)#отладка