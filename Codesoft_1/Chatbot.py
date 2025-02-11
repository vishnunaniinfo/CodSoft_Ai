import json
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download stopwords if not already downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Load responses from JSON file
with open("responses.json", "r") as file:
    responses = json.load(file)

# Preprocess user input (remove stopwords & special characters)
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)  # Remove special characters
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    return " ".join(tokens)

# Get chatbot response using NLP matching
def get_response(user_input):
    user_input = preprocess_text(user_input)
    for key in responses.keys():
        if key in user_input:
            return responses[key]
    return "I'm not sure about that. Can you ask something related to cybersecurity?"

# Run chatbot in terminal
if __name__ == "__main__":
    print("🔒 Cybersecurity Chatbot: Type 'exit' to stop")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Stay safe online! 🔐")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")
