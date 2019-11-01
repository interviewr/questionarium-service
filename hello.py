from flask import Flask, jsonify, request
app = Flask(__name__)

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
