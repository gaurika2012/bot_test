from flask import Flask, request, jsonify
import difflib
from intents import TRAVEL_INTENTS

app = Flask(__name__)

def get_intent(user_input):
    user_input = user_input.lower()
    for intent, data in TRAVEL_INTENTS.items():
        matches = difflib.get_close_matches(user_input, data["examples"], n=1, cutoff=0.5)
        if matches:
            return data["response"]
    return "Sorry, I didn’t quite catch that. Can you rephrase?"

@app.route('/')
def home():
    return "🌍 TravelBot is running! Try POSTing to /chat"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get("message", "")
    response = get_intent(message)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)