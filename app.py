from flask import Flask, request, jsonify
from intents import TRAVEL_INTENTS  # Or define directly in app.py

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").lower()
    
    # Match known phrases
    for key_phrase, response in TRAVEL_INTENTS.items():
        if key_phrase in user_message:
            return jsonify({"reply": response})

    # Default response
    return jsonify({"reply": "I'm not sure, but I can help with common travel questions. Try asking about destinations, routes, or tips."})

import os

port = int(os.environ.get("PORT", 5000))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)
