from flask import Flask, render_template

app = Flask(__name__)#создание приложения

@app.route('/')#главная страница
def index():#функция
    return render_template('index.html')#приветственное сообщение

@app.route('/blog')#страница блога
def blog():
    return render_template('blog.html')#сообщение о блогах

@app.route('/contacts')#страница контактов
def contacts():#контактная информация
    return render_template('contacts.html')#меню для навигации

if __name__ == '__main__':#запуск приложения
    app.run(debug=True)#отладка