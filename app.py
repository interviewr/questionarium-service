from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:password@localhost/questionarium'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:password@localhost/questionarium'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#### Models ####
class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    answer = db.Column(db.String())
    category = db.Column(db.String())

    def __init__(self, title, answer, category):
        self.title = title
        self.answer = answer
        self.category = category

#### Schemas ####
class QuestionSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    answer = fields.Str()
    category = fields.Str()

questions_schema = QuestionSchema(many=True)

default_category = 'javascript'

@app.route('/health')
def health():
    state = {"status": "UP"}
    return jsonify(state)

@app.route('/questions', methods=['GET'])
def get_questions():
    questions = Question.query.all()
    result = questions_schema.dump(questions)
    return {"questions": result}

@app.route('/questions', methods=['POST'])
def create_question():
    req_data = request.get_json()
    data = Question(req_data['title'], req_data['answer'], req_data['category'])
    db.session.add(data)
    db.session.commit()
    return ''

if __name__ == '__main__':
    app.run()
