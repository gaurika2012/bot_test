from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Your bot is live! Try sending a POST request to /chat"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get("message", "")
    return jsonify({"response": f"You said: {message}"})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)