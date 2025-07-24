from flask import Flask, request, jsonify, render_template
import openai
import os

app = Flask(__name__)

# Load OpenAI API key from environment
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return render_template("index.html")  # Shows your chatbot UI

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    
    # Send to OpenAI GPT
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Or gpt-4 if you have access
            messages=[
                {"role": "system", "content": "You are a helpful chatbot."},
                {"role": "user", "content": user_message}
            ]
        )
        reply = response["choices"][0]["message"]["content"]
    except Exception as e:
        reply = f"Error: {str(e)}"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

