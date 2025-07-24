from flask import Flask, request, jsonify, render_template
import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv(openai.api_key = os.getenv("OPENAI_API_KEY")")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]
        )
        reply = response.choices[0].message.content.strip()
    except Exception as e:
        reply = "Oops! Something went wrong. 😢"

    return jsonify({"reply": reply})
