# 41.Write a Flask route that accepts a parameter in the URL and displays it on the page.
from flask import Flask

question41 = Flask(__name__)

@question41.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'

if __name__ == '__main__':
    question41.run(debug=True)
