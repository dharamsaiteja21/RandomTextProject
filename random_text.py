from flask import Flask, jsonify
import random

app = Flask(__name__)

def generate_random_text():
    words = ["Python", "GitHub", "Code", "Project", "OpenAI", "AI", "ChatGPT", "Random", "Text", "Generator"]
    sentence = " ".join(random.choices(words, k=5))
    return sentence

@app.route('/')
def home():
    return "Hello from EC2"

@app.route('/generate', methods=['GET'])
def generate():
    random_text = generate_random_text()
    return jsonify({"random_text": random_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

