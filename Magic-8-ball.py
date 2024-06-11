from flask import Flask, render_template, request
import random

app = Flask(__name__)

# List of possible decisions
decisions = [
    "Yes, definitely.",
    "No, certainly not.",
    "Maybe.",
    "Ask again later.",
    "It is certain.",
    "Very doubtful.",
    "Cannot predict now.",
    "Absolutely!",
    "Better not tell you now.",
    "Concentrate and ask again."
]

def get_random_decision():
    """Select and return a random decision from the list."""
    return random.choice(decisions)

@app.route('/', methods=['GET', 'POST'])
def index():
    decision = None
    if request.method == 'POST':
        question = request.form['question']
        if question:
            decision = get_random_decision()
    return render_template('index.html', decision=decision)

if __name__ == "__main__":
    app.run(debug=True)
