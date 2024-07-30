# 43.Describe the process of connecting a Flask app to a SQLite database using SQLAIchemy.
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

@app.route('/create')
def create_db():
    db.create_all()
    return 'Database created!'

if __name__ == '__main__':
    app.run(debug=True)
