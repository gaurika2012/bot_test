TRAVEL_INTENTS = {
    "weather": {
        "examples": ["what’s the weather", "is it hot", "weather in paris", "do I need an umbrella"],
        "response": "Let me check the current weather for you...",
        "action": "get_weather"
    },
    "hotels": {
        "examples": ["show me hotels", "where can I stay", "recommend hotels"],
        "response": "Here are some great hotel options!",
        "action": "show_hotels"
    },
    "time": {
        "examples": ["what time is it in paris", "local time", "current time paris"],
        "response": "Sure, let me check the time in Paris...",
        "action": "get_local_time"
    },
    "recommendation": {
        "examples": ["where should I go", "suggest travel destinations", "best places to visit"],
        "response": "Here are some amazing travel destinations you might like:",
        "action": "suggest_destinations"
    }
}

