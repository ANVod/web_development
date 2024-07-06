from flask import Flask

# Создаем экземпляр класса Flask (переменную app)
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Импортируем маршруты после создания экземпляра app
from app import routes