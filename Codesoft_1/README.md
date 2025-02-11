# 🔒 Cybersecurity Chatbot  
A simple **rule-based chatbot** that provides answers to common **cybersecurity-related questions**.  
It is built using **Python, Flask, and NLTK**, with predefined responses stored in a JSON file.  

---

## 📌 **Features**
✅ Answers cybersecurity questions like phishing, malware, strong passwords, and more  
✅ Uses **Natural Language Processing (NLP)** for better query understanding  
✅ Runs as a **web application** using **Flask**  
✅ Easy to expand with more cybersecurity topics  

---

## 📌 **Project Structure**

📂 chatbot/ ├── app.py # Flask application ├── chatbot.py # Chatbot logic (NLP processing) 
├── responses.json # Predefined chatbot responses ├── 📂 templates/ # HTML templates │ ├── index.html # Chat UI


---

## 📌 **Installation & Setup**
### **1️⃣ Install Dependencies**  
Ensure you have Python installed. Then, install the required libraries:  
```bash
pip install flask nltk
                2️⃣ Run the Chatbot
                                 python app.py
**Once the server starts, open your browser and visit:
👉 http://127.0.0.1:5000/

📌 How It Works
The chatbot loads responses from responses.json.
Uses NLTK for text processing (removing stopwords, handling queries).
The Flask web app provides a simple chat interface.
Users enter a question, and the bot responds based on predefined rules.
📌 Example Questions
❓ What is phishing?
❓ How do I create a strong password?
❓ What is malware?
❓ Is public Wi-Fi safe?
❓ What is a firewall?

📌 Future Improvements
✅ Add Machine Learning (ML) for smarter responses
✅ Deploy on Heroku / Render for online access
✅ Support voice input



📌 Connect & Support
If you find this project useful, feel free to ⭐ star this repository on GitHub!
For any questions, reach out via LinkedIn: [Your Profile Link]

🚀 Made with ❤️ by Vishnu Vardhan Burri

