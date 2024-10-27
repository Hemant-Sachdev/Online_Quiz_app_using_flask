from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample questions and answers
questions = {
    1: {"num": 1, "question": "What is the output of print(2 ** 3)?", "options": ["5", "6", "8", "9"], "answer": "8"},
    2: {"num": 2, "question": "Which of the following is a mutable data type in Python?", "options": ["List", "Tuple", "String", "Integer"], "answer": "List"},
    3: {"num": 3, "question": "What is the correct way to define a function in Python?", "options": ["function myFunc()", "def myFunc():", "create myFunc():", "define myFunc():"], "answer": "def myFunc():"},
    4: {"num": 4, "question": "Which keyword is used to create a class in Python?", "options": ["class", "def", "function", "object"], "answer": "class"},
    5: {"num": 5, "question": "What is the output of len([1, 2, 3])?", "options": ["1", "2", "3", "None"], "answer": "3"}
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    total_score = 0
    correct_answers = 0

    for question_id, question_data in questions.items():
        selected_option = request.form.get(str(question_id))
        if selected_option == question_data["answer"]:
            total_score += 1
            correct_answers += 1

    return render_template('result.html', score=total_score, total=len(questions))

if __name__ == '__main__':
    app.run(debug=True)
