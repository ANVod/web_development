from flask import Flask, render_template, redirect, url_for, flash, request
from forms import EditProfileForm
from models import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Mocking a user for demonstration purposes
current_user = User(name="John Doe", email="john@example.com", password="password123")

@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.email = form.email.data
        current_user.password = form.password.data
        flash('Your profile has been updated!', 'success')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.name.data = current_user.name
        form.email.data = current_user.email
    return render_template('edit_profile.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)