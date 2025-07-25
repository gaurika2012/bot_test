import difflib
from intents import TRAVEL_INTENTS

def get_intent(user_input):
    user_input = user_input.lower()
    for intent, data in TRAVEL_INTENTS.items():
        matches = difflib.get_close_matches(user_input, data["examples"], n=1, cutoff=0.5)
        if matches:
            return data["response"]
    return "Sorry, I didn’t quite catch that. Can you rephrase?"