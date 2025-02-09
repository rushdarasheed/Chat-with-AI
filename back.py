from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

# Set up the API key
genai.configure(api_key="AIzaSyBqNrCj_KKr0FXKTgKWoL2y0cpoWdR7cA0")

# Initialize the AI model
model = genai.GenerativeModel("gemini-pro")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    response = model.generate_content(user_input)
    return jsonify({"response": response.text})

if __name__ == '__main__':
    app.run(debug=True)
