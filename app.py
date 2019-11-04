from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/lexus'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/lexus'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    answer = db.Column(db.String())

    def __init__(self, title, answer):
        self.title = title
        self.answer = answer

default_category = 'javascript'
questions = [
    {
        'id': 1,
        'title': 'Sample title',
        'answer': 'Sample answer',
        'category': 'javascript'
    },
    {
        'id': 2,
        'title': 'Sample title',
        'answer': 'Sample answer',
        'category': 'python'
    }
]

@app.route('/health')
def health():
    state = {"status": "UP"}
    return jsonify(state)

@app.route('/questions', methods=['GET'])
def get_questions():
    category = request.args.get('category', default_category)
    filtered_questions = list(filter(lambda x: x['category'] == category, questions))
    return jsonify(filtered_questions)

@app.route('/questions', methods=['POST'])
def create_question():
    return ''

if __name__ == '__main__':
    app.run()
