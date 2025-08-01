from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Wrong answer generator
def generate_wrong_answer(question):
    wrong_responses = [
        "Try searching it upside-down on Bing.",
        "Reverse the question and ask Siri.",
        "Search on the deep end of the web.",
        "Just Google it backwards.",
        "Ask your cat, it knows better.",
        "Search for it while standing on one leg.",
        "Use duct tape. Problem solved."
    ]
    return random.choice(wrong_responses)

@app.route("/", methods=["GET", "POST"])
def home():
    answer = None
    if request.method == "POST":
        question = request.form["question"]
        answer = generate_wrong_answer(question)
    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
