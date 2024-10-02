import random
import nltk
from nltk.chat.util import Chat, reflections

# Ensure you have NLTK installed and the necessary resources downloaded
# nltk.download('punkt')

# Define some sample pairs of user input and bot responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I assist you today?", "Hi there! What can I do for you?", "Hey! How may I help you?"]
    ],
    [
        r"what is your name?",
        ["I am Basit, your virtual assistant!", "You can call me Basit!", "My name is Basit, here to help you."]
    ],
    [
        r"what do you do?",
        ["I assist with customer support and provide information about Toutche and its products.", 
         "I'm here to help you with any questions about Toutche's products and services."]
    ],
    [
        r"tell me about Heileo electric bicycles",
        ["The Heileo range includes various models designed for comfort and efficiency.", 
         "Heileo bicycles are known for their innovative features and eco-friendly designs."]
    ],
    [
        r"what are the main customer support challenges?",
        ["Some challenges include timely responses to inquiries and providing accurate information.", 
         "Ensuring customer satisfaction while managing high volumes of inquiries can be challenging."]
    ],
    [
        r"how can you help me with my order?",
        ["I can provide updates on your order status, help with tracking, and address any concerns you may have.",
         "Just give me your order number, and I can assist you with that."]
    ],
    [
        r"help|support",
        ["I'm here to help! Please describe your issue, and I'll do my best to assist you.", 
         "What kind of support do you need today?"]
    ],
    [
        r"bye|exit|quit",
        ["Goodbye! If you have more questions, feel free to ask anytime.", 
         "See you later! Have a great day!"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I didn't understand that. Can you please rephrase?", 
         "Could you clarify what you mean? I'm here to help."]
    ]
]

# Create a chatbot
class BasitChatbot:
    def __init__(self, pairs):
        self.chatbot = Chat(pairs, reflections)

    def start_chat(self):
        print("Hello! I am Basit, your virtual assistant. Type 'quit' to exit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("Basit: Goodbye! If you have more questions, feel free to ask anytime.")
                break
            response = self.chatbot.respond(user_input)
            print(f"Basit: {response if response else 'I am still learning. Please ask something else.'}")

if __name__ == "__main__":
    basit = BasitChatbot(pairs)
    basit.start_chat()
