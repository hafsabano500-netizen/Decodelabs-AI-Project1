
from datetime import datetime
import random

print("=" * 65)
print("🤖 Welcome to Smart AI ChatBot")
print("I am your virtual assistant and learning companion.")
print("Type 'help' to see all available commands.")
print("Type 'bye' to exit the chatbot.")
print("=" * 65)

greetings = [
    "Hello! How can I assist you today?",
    "Hi there! Nice to meet you.",
    "Hey! What can I do for you today?"
]

motivation_quotes = [
    "Success comes from consistency and hard work.",
    "Keep learning because knowledge is your greatest asset.",
    "Dream big and work hard to achieve your goals.",
    "Every expert was once a beginner."
]

while True:
    user_input = input("\nYou: ").lower().strip()

    # Exit condition
    if user_input in ["bye", "goodbye", "exit", "quit"]:
        print("Bot: Goodbye! Keep learning and have a wonderful day. 😊")
        break

    # Greetings
    elif user_input in ["hi", "hello", "hey"]:
        print("Bot:", random.choice(greetings))

    # How are you
    elif "how are you" in user_input:
        mood = input("Bot: I'm doing great! How are you feeling today? ").lower()

        if mood in ["good", "fine", "great", "happy"]:
            print("Bot: That's wonderful to hear! 😊")
        elif mood in ["sad", "bad", "upset"]:
            print("Bot: Don't worry. Every difficult moment will pass. Stay positive! 💪")
        else:
            print("Bot: Thanks for sharing your feelings with me.")

    # Name
    elif "what is your name" in user_input:
        print("Bot: My name is Smart AI ChatBot.")

    # Creator
    elif "who created you" in user_input:
        print("Bot: I was created by a DecodeLabs AI Intern using Python.")

    # AI
    elif "what is artificial intelligence" in user_input:
        print("Bot: Artificial Intelligence is a field of computer science")
        print("Bot: that enables machines to perform tasks requiring human intelligence.")

    # Machine Learning
    elif "what is machine learning" in user_input:
        print("Bot: Machine Learning is a branch of AI that allows")
        print("Bot: computers to learn from data and improve automatically.")

    # Python
    elif "what is python" in user_input:
        print("Bot: Python is a powerful programming language widely")
        print("Bot: used in AI, Data Science, and Web Development.")

    # Time
    elif "what is the current time" in user_input:
        current_time = datetime.now().strftime("%I:%M %p")
        print("Bot: The current time is", current_time)

    # Date
    elif "what is today's date" in user_input:
        current_date = datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's date is", current_date)

    # Study Tips
    elif "can you give me study tips" in user_input:
        print("Bot: Here are some study tips:")
        print("1. Study consistently.")
        print("2. Practice daily.")
        print("3. Focus on understanding concepts.")
        print("4. Take short breaks while studying.")

    # Motivation
    elif "can you motivate me" in user_input:
        print("Bot:", random.choice(motivation_quotes))

    # Skills
    elif "what skills are required for artificial intelligence" in user_input:
        print("Bot: Important AI skills include:")
        print("- Python")
        print("- SQL")
        print("- Machine Learning")
        print("- Problem Solving")
        print("- Data Analysis")

    # Internship
    elif "why are internships important" in user_input:
        print("Bot: Internships provide practical experience,")
        print("Bot: improve your skills, and help build a strong portfolio.")

    # Career
    elif "how can i become an ai engineer" in user_input:
        print("Bot: Learn Python, Machine Learning, Data Structures,")
        print("Bot: and build projects to strengthen your portfolio.")

    # Favorite Language
    elif "what is your favorite programming language" in user_input:
        print("Bot: My favorite programming language is Python because")
        print("Bot: it is simple, powerful, and widely used in AI.")

    # Thank You
    elif "thank you" in user_input:
        print("Bot: You're welcome! Happy to help. 😊")

    # Help
    elif user_input == "help":
        print("\n========== AVAILABLE COMMANDS ==========")
        print("Hi")
        print("How are you?")
        print("What is your name?")
        print("Who created you?")
        print("What is Artificial Intelligence?")
        print("What is Machine Learning?")
        print("What is Python?")
        print("What is the current time?")
        print("What is today's date?")
        print("Can you give me study tips?")
        print("Can you motivate me?")
        print("What skills are required for Artificial Intelligence?")
        print("Why are internships important?")
        print("How can I become an AI Engineer?")
        print("What is your favorite programming language?")
        print("Thank you")
        print("Bye")
        print("========================================")

    # Unknown command
    else:
        print("Bot: Sorry, I don't understand that.")
        print("Bot: Please type 'help' to see the available commands.")