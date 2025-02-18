import json
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from werkzeug.security import check_password_hash
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user

app = Flask(__name__)

app.secret_key = 'mysecretkey'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(id=user_id)

class LoginForm(FlaskForm):
    username = StringField('username')
    password = PasswordField('password')

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    db = json.load(open('users.json', 'r'))
    if request.method == 'POST':
        username = form.username.data
        (id, pw_hash), = [(x['id'], x['pw']) for x in db if x['name'] == username]
        pw_auth = check_password_hash(pwhash=pw_hash, password=form.password.data)
        if pw_auth:
            user = User(id=id)
            login_user(user, remember=True)
            return redirect(url_for('index'))
        msg = 'Your name or password does not match!'
        return render_template('login.html', form=form, msg=msg)
    return render_template('login.html', form=form, msg='')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

import click

@click.command('test-command')
def init_test_command():
    click.echo('Initialized the database.')

def init_app(app):
    app.cli.add_command(init_test_command)

init_app(app)

if __name__ == '__main__':
    app.debug=True
    app.run()