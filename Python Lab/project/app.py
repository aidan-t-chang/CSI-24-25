from flask import Flask, render_template, request
app = Flask(__name__)


# Define a list of quiz questions and their corresponding options
# Each question will have a list of options and a dictionary to track scores


questions = [ #The higher point totals are leading to an answer of "artist" and the lower ones will give you "scientist"
    {
        'question': 'What do you like to do outside of school?',
        'options': ['Homework...', 'Read!', 'Sleep', 'Draw'],
        'scores': {'Homework...': 1, 'Read': 2, 'Sleep': 3, 'Draw': 4}
    },
    {
        'question': 'What class is your favorite?',
        'options': ['Science', 'Math', 'History', 'Art'],
        'scores': {'Science': 1, 'Math': 2, 'History': 3, 'Art': 4}
    },
    {
        'question': 'Where do you want to live?',
        'options': ['In the city', 'In a suburb', 'In a small town', 'In the mountains'],
        'scores': {'In the city': 1, 'In a suburb': 2, 'In a small town': 3, 'In the mountains': 4}
    },
    {
        'question': 'Do you like working with others?',
        'options': ['I can, it depends', 'I love working with people', 'Absolutely not', 'Sure'],
        'scores': {'I can, it depends': 1, 'I love working with people': 2, 'Absolutely not': 3, 'Sure': 4}
    },
    {
        'question': 'Do you like working with computers?',
        'options': ['I can, but I would not say I prefer it', 'Yes!', 'Absolutely not', 'If I so much as look at a computer it breaks'],
        'scores': {'I can, but I would not say I prefer it': 1, 'Yes!': 2, 'Absolutely not': 3, 'If I so much as look at a computer it breaks': 4}
    }
]


# Define results based on scores
results = {
    5: "You should be a scientist!",
    6: "You should be a scientist!",
    7: "You should be a scientist!",
    8: "You should be a scientist!",
    9: "You should be a scientist!",
    10: "You should be a doctor! ",
    11: "You should be a doctor!",
    12: "You should be a doctor!",
    13: "You should be a doctor!",
    14: "You should be a doctor!",
    15: "You should be an engineer!",
    16: "You should be an engineer!",
    17: "You should be an engineer!",
    18: "You should be an engineer!",
    19: "You should be an engineer",
    20: "You should be an artist!"
}
#All results possible results point to 1 of 4 answers


@app.route('/', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        # Calculate the score based on the answers
        score = 0 #the score starts at 0 and adds each point total to it
        for idx, question in enumerate(questions):
            answer = request.form.get(f'question{idx}')
            score += question['scores'].get(answer, 0)


        # Calculate the result based on the score
        result = results.get(score, "You are unique! Find your own path.") #The 'unique' text won't be seen, because all possible combinations of scores are defined
        if 5 <= score <= 9:
            return render_template('scientist.html', result=result)
        elif 10 <= score <= 14:
            return render_template('doctor.html', result=result)
        elif 15 <= score <= 19:
            return render_template('engineer.html', result=result)
        else:
            return render_template('artist.html', result=result)


    return render_template('index.html', questions=questions)


if __name__ == '__main__':
    app.run(debug=True)


