from flask import Flask, render_template, request
import json
import chatbot  # Import the chatbot logic

app = Flask(__name__)

# Load chatbot responses
with open("responses.json", "r") as file:
    responses = json.load(file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_input = request.form["msg"]
    response = chatbot.get_response(user_input)
    return response

if __name__ == "__main__":
    app.run(debug=True)
