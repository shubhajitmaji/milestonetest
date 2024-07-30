# 40.Explain how to set up a Flask application to handle form submissions using POST requests
from flask import Flask, request, render_template

question40 = Flask(__name__)

@question40.route('/')
def index():
    return render_template('form.html')

@question40.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    return f'Hello, {username}!'

if __name__ == '__main__':
    question40.run(debug=True)
