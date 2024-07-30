# 39.How would you create a basic Flask route that displays "Hello, World!" on the homepage?
from flask import Flask

question39 = Flask(__name__)

@question39.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    question39.run(debug=True)