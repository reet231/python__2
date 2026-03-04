# ============================================================
# Simple Chatbot - CS24078
# Skills: String manipulation, conditional statements, loops
# ============================================================

# Dictionary mapping keywords to responses
responses = {
    # Greetings
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! What can I do for you?",
    "hey": "Hey! Nice to meet you. How can I assist?",
    "good morning": "Good morning! Hope you have a great day ahead!",
    "good evening": "Good evening! How can I help you tonight?",

    # Farewells
    "bye": "Goodbye! Have a wonderful day!",
    "goodbye": "See you later! Take care!",
    "exit": "Exiting chat. Goodbye!",
    "quit": "Quitting chat. Bye!",

    # How are you
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "what's up": "Not much! Just here to chat. What can I help you with?",

    # About the bot
    "who are you": "I am a simple chatbot created for CS24078. I use predefined responses to assist you.",
    "what are you": "I'm a rule-based chatbot that maps your inputs to predefined responses.",
    "what can you do": "I can answer basic questions, chat with you, and provide information on common topics!",

    # Help
    "help": "Sure! You can ask me about: greetings, my identity, weather, jokes, time, or just chat!",

    # Weather
    "weather": "I don't have live data, but I hope it's sunny where you are! ☀️",
    "temperature": "I can't check real-time temperature, but stay cool (or warm)! 😄",

    # Jokes
    "joke": "Why don't scientists trust atoms? Because they make up everything! 😄",
    "funny": "Here's one: Why did the programmer quit? Because he didn't get arrays! 😂",

    # Time / Date
    "time": "I don't have a clock, but your device can show you the current time!",
    "date": "I can't fetch the date, but check the bottom-right of your screen!",

    # Name
    "your name": "I'm ChatBot, your friendly assistant built in Python!",
    "name": "My name is ChatBot! What's yours?",

    # Thanks
    "thank you": "You're welcome! 😊 Is there anything else I can help you with?",
    "thanks": "Happy to help! Let me know if you need anything else.",

    # Default
    "default": "Hmm, I'm not sure I understand that. Could you rephrase? Type 'help' to see what I can do."
}


def get_response(user_input):
    """
    Process user input using string manipulation and keyword detection.
    Returns an appropriate predefined response.
    """
    # String manipulation: convert to lowercase and strip whitespace
    user_input = user_input.lower().strip()

    # Remove punctuation for better matching
    cleaned_input = ""
    for char in user_input:
        if char.isalnum() or char == " ":
            cleaned_input += char
    cleaned_input = cleaned_input.strip()

    # Direct match check
    if cleaned_input in responses:
        return responses[cleaned_input]

    # Keyword detection: check if any keyword exists in the user input
    for keyword in responses:
        if keyword in cleaned_input:
            return responses[keyword]

    # No match found - return default response
    return responses["default"]


def chatbot():
    """
    Main chatbot function with conversational loop.
    Uses loops and conditional statements for interaction.
    """
    print("=" * 50)
    print("   Welcome to Simple ChatBot - CS24078")
    print("=" * 50)
    print("Type 'bye', 'exit', or 'quit' to end the chat.")
    print("Type 'help' to see available topics.\n")

    # Loop to keep conversation going
    while True:
        # Get user input
        user_input = input("You: ")

        # Conditional check: skip empty input
        if not user_input.strip():
            print("ChatBot: Please type something! I'm listening. 😊\n")
            continue

        # Conditional check: exit keywords
        exit_keywords = ["bye", "goodbye", "exit", "quit"]
        user_lower = user_input.lower().strip()

        if any(keyword in user_lower for keyword in exit_keywords):
            print("ChatBot:", get_response(user_lower))
            print("\nThank you for chatting! Goodbye! 👋")
            break

        # Get and display response
        response = get_response(user_input)
        print(f"ChatBot: {response}\n")


# ============================================================
# Entry point
# ============================================================
if __name__ == "__main__":
    chatbot()
