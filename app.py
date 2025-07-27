from flask import Flask, request, jsonify, render_template
from intents import TRAVEL_INTENTS
import difflib
import datetime

app = Flask(__name__)

# --------- Smart Action Functions --------- #

def get_weather():
    # Placeholder weather response (you can connect to real APIs later)
    return "🌦️ It’s currently 72°F and partly cloudy in Paris."

def show_hotels():
    # Placeholder hotel listings
    return (
        "🏨 **Top Hotels in Paris:**\n"
        "- Hotel Luna – 4★ – $120/night\n"
        "- CozyNest – 3★ – $90/night\n"
        "- CityScape Suites – 5★ – $200/night"
    )

def get_local_time():
    # Simulated local time
    paris_time = datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    return f"🕒 The current time in Paris is {paris_time.strftime('%I:%M %p')}."

def suggest_destinations():
    return (
        "✈️ Here are some popular travel destinations:\n"
        "- 🇫🇷 Paris: Art, food, romance\n"
        "- 🇯🇵 Tokyo: Culture, tech, sushi\n"
        "- 🇺🇸 New York: Energy, museums, skyline\n"
        "- 🇮🇳 Jaipur: History, palaces, food"
    )

SMART_ACTIONS = {
    "get_weather": get_weather,
    "show_hotels": show_hotels,
    "get_local_time": get_local_time,
    "suggest_destinations": suggest_destinations
}

# --------- Intent Matching --------- #

def get_intent(user_input):
    user_input = user_input.lower()
    for intent, data in TRAVEL_INTENTS.items():
        matches = difflib.get_close_matches(user_input, data["examples"], n=1, cutoff=0.5)
        if matches:
            return intent, data
    return None, {"response": "❓ Sorry, I didn’t quite catch that. Can you rephrase?"}

# --------- Routes --------- #

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    
    intent_key, intent_data = get_intent(user_message)
    bot_response = intent_data["response"]

    # If there's a smart action, trigger it
    if "action" in intent_data:
        action_func = SMART_ACTIONS.get(intent_data["action"])
        if action_func:
            smart_reply = action_func()
            bot_response += "\n\n" + smart_reply

    return jsonify({"response": bot_response})

# --------- Run the App --------- #

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
