import spacy
import random

nlp = spacy.load("en_core_web_md")

print("🤖 Welcome! Type 'exit' or 'quit' to leave.\n")

intents = {
    "greeting": {
        "keywords": ["hello", "hi", "hey", "good morning", "good evening"],
        "response": "Hello! How can I help you today?"
    },
    "goodbye": {
        "keywords": ["bye", "goodbye", "see you", "exit", "quit"],
        "response": "Goodbye! Have a great day!"
    },
    "thanks": {
        "keywords": ["thanks", "thank you", "thx"],
        "response": "You're welcome! 😊"
    },
    "story": {
        "keywords": ["story", "tell me a story", "5 line story", "short story"],
        "response": (
            "Once there was a star that couldn't shine. "
            "A child smiled at it. Suddenly, it glowed bright. "
            "Everyone saw it and smiled. The star was never alone again."
        )
    },
    "advice": {
        "keywords": ["give me advice", "any suggestions", "what should I do"],
        "response": "Stay positive, keep learning, and don't give up! 🚀"
    },
    "compliment": {
        "keywords": ["say something nice", "give me a compliment", "make me smile"],
        "response": "You're amazing just the way you are! 🌟"
    },
    "creator": {
        "keywords": ["who made you", "your creator", "who created you"],
        "response": "I was built by a Python programmer using spaCy and some magic 🧠✨"
    },
    "weather": {
        "keywords": ["weather", "today's weather", "rain", "sunny"],
        "response": "I can't check live weather now, but it's always sunny in here ☀️"
    },
    "help": {
        "keywords": ["help", "i need help", "can you assist me"],
        "response": "Of course! Ask me anything – I’ll try my best to answer."
    },
    "identity": {
        "keywords": ["who are you", "what is your name", "tell me about yourself"],
        "response": "I'm your friendly chatbot 🤖 here to help you out!"
    },
    "joke": {
        "keywords": ["joke", "make me laugh", "say something funny"],
        "responses": [
            "Why did the math book look sad? Because it had too many problems! 🤓",
            "Why don’t scientists trust atoms? Because they make up everything! 😄",
            "Why did the scarecrow win an award? Because he was outstanding in his field! 🌾"
        ]
    },
    "funfact": {
        "keywords": ["fun fact", "tell me something interesting", "interesting fact"],
        "responses": [
            "Did you know? Octopuses have three hearts! 🐙",
            "Bananas are berries, but strawberries aren't! 🍌🍓",
            "Honey never spoils — archaeologists found 3,000-year-old honey in Egyptian tombs!"
        ]
    },
    "default": {
        "response": "I'm not sure how to respond to that. Can you ask something else?"
    }
}

processed_intents = [
    (intent, nlp(kw))
    for intent, data in intents.items()
    if "keywords" in data
    for kw in data["keywords"]
]

exact_match_map = {}
for intent, data in intents.items():
    if "keywords" in data:
        for phrase in data["keywords"]:
            if "response" in data:
                exact_match_map[phrase.lower()] = data["response"]
            elif "responses" in data:
                exact_match_map[phrase.lower()] = random.choice(data["responses"])

SIM_THRESHOLD = 0.6

# Chat loop
while True:
    user_input = input("You: ").strip().lower()
    if user_input in ["exit", "quit"]:
        print("Chatbot:", intents["goodbye"]["response"])
        break

    if user_input in exact_match_map:
        print("Chatbot:", exact_match_map[user_input])
        continue

    user_doc = nlp(user_input)
    best_intent = None
    best_score = SIM_THRESHOLD

    for intent, key_doc in processed_intents:
        score = user_doc.similarity(key_doc)
        if score > best_score:
            best_intent = intent
            best_score = score

    if best_intent:
        intent_data = intents[best_intent]
        if "response" in intent_data:
            print("Chatbot:", intent_data["response"])
        elif "responses" in intent_data:
            print("Chatbot:", random.choice(intent_data["responses"]))
    else:
        print("Chatbot:", intents["default"]["response"])
