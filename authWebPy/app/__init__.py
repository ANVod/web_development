from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required, LoginManager
from werkzeug.security import generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))

    # другие поля и методы

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    if request.method == 'POST':
        new_name = request.form.get('name')
        new_email = request.form.get('email')
        new_password = request.form.get('password')

        # Обновление данных пользователя
        user = current_user
        user.name = new_name
        user.email = new_email
        if new_password:
            user.password = generate_password_hash(new_password, method='sha256')

        # Сохранение изменений в базе данных
        db.session.commit()

        flash('Your profile has been updated!', 'success')
        return redirect(url_for('profile'))

    return render_template('edit_profile.html', user=current_user)


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)


if __name__ == "__main__":
    app.run(debug=True)
