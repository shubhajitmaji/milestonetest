# 42.How can you implement user authentication in a Flask application?
from flask import Flask, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

question42 = Flask(__name__)
question42.secret_key = 'secret_key'
login_manager = LoginManager()
login_manager.init_app(question42)

class User(UserMixin):
    def __init__(self, id):
        self.id = id

users = {'user': {'password': 'password'}}

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@question42.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if users.get(username) and users[username]['password'] == password:
            user = User(username)
            login_user(user)
            return redirect(url_for('protected'))
    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

@question42.route('/protected')
@login_required
def protected():
    return f'Hello, {current_user.id}!'

@question42.route('/logout')
def logout():
    logout_user()
    return 'Logged out!'

if __name__ == '__main__':
    question42.run(debug=True)
