from flask import render_template, request, flash, redirect, url_for
from app import app


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        age = request.form.get('age')

        if not name or not city or not hobby or not age:
            flash('Please fill out all fields')
        else:
            flash(f'Name: {name}, City: {city}, Hobby: {hobby}, Age: {age}')

    return render_template('index.html')