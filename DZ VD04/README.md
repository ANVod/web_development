```markdown
# Flask Project

Это простой проект на Flask, который включает три страницы: главная, блог и контакты. Все страницы содержат меню для навигации.

## Установка

1. Клонируйте репозиторий или создайте новую директорию и перейдите в нее:

    ```bash
    mkdir flask_project
    cd flask_project
    ```

2. Создайте виртуальную среду и активируйте ее:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Для Windows используйте `venv\Scripts\activate`
    ```

3. Установите Flask:

    ```bash
    pip install Flask
    ```

## Структура проекта

Проект имеет следующую структуру:

```
flask_project/
│
├── static/
│
├── templates/
│   ├── index.html
│   ├── blog.html
│   └── contacts.html
│
└── app.py
```

## Запуск приложения

1. Убедитесь, что вы находитесь в виртуальной среде.
2. Запустите приложение:

    ```bash
    python app.py
    ```

3. Откройте веб-браузер и перейдите по адресу [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Описание страниц

### Главная страница

Файл: `templates/index.html`

Содержит приветственное сообщение и меню для навигации.

### Страница блога

Файл: `templates/blog.html`

Содержит сообщение о блогах и меню для навигации.

### Страница контактов

Файл: `templates/contacts.html`

Содержит контактную информацию и меню для навигации.

## Пример кода

### app.py

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run(debug=True)
```

### index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home Page</title>
</head>
<body>
    <nav>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/blog">Blog</a></li>
            <li><a href="/contacts">Contacts</a></li>
        </ul>
    </nav>
    <h1>Welcome to the Home Page!</h1>
    <p>This is the main page of the website.</p>
</body>
</html>
```

### blog.html

```html
<!DOCTYPE

html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog Page</title>
</head>
<body>
    <nav>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/blog">Blog</a></li>
            <li><a href="/contacts">Contacts</a></li>
        </ul>
    </nav>
    <h1>Welcome to the Blog Page!</h1>
    <p>Here you can find various blog posts.</p>
</body>
</html>
```

### contacts.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contacts Page</title>
</head>
<body>
    <nav>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/blog">Blog</a></li>
            <li><a href="/contacts">Contacts</a></li>
        </ul>
    </nav>
    <h1>Welcome to the Contacts Page!</h1>
    <p>Contact us at contact@example.com.</p>
</body>
</html>
```

## Автор

Антон Водясов

## Лицензия

Этот проект лицензирован под лицензией MIT. Подробности см. в файле `LICENSE`.
```

