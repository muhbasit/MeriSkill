import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK datasets (only the first time)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Simple intent detection keywords
INTENTS = {
    'greet': ['hello', 'hi', 'hey', 'greetings'],
    'goodbye': ['bye', 'goodbye', 'see you'],
    'thank': ['thanks', 'thank you'],
    'query': ['what', 'how', 'why', 'where', 'who'],
    'helio': ['helio', 'electric bike', 'e-bike', 'bicycle', 'electric bicycles']
}

# Tokenize the user input
def tokenize_input(user_input):
    return word_tokenize(user_input)

# Perform part-of-speech tagging
def pos_tagging(tokens):
    return pos_tag(tokens)

# Lemmatize tokens based on POS tags
def lemmatize_tokens(tokens):
    lemmatized = []
    for word, tag in tokens:
        pos = get_wordnet_pos(tag)
        lemmatized.append(lemmatizer.lemmatize(word, pos) if pos else word)
    return lemmatized

# Map NLTK POS tags to WordNet POS tags for lemmatization
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wn.ADJ
    elif treebank_tag.startswith('V'):
        return wn.VERB
    elif treebank_tag.startswith('N'):
        return wn.NOUN
    elif treebank_tag.startswith('R'):
        return wn.ADV
    else:
        return None

# Simple intent detection based on keywords
def detect_intent(tokens):
    for intent, keywords in INTENTS.items():
        if any(word in tokens for word in keywords):
            return intent
    return 'unknown'

# Generate a response based on the detected intent
def generate_response(intent):
    responses = {
        'greet': "Hello! My name is Basit. How can I assist you today?",
        'goodbye': "Goodbye! Have a great day!",
        'thank': "You're welcome!",
        'query': "That's a great question! Let me find the answer for you.",
        'helio': """Helio Electric Bicycles are designed for effortless and eco-friendly cycling. They feature motor assistance for easier rides, powerful lithium-ion batteries for long distances, and various models suited for commuting, off-road adventures, and portability. With ranges up to 60 miles, they provide a greener alternative to cars while offering customizable modes for different rides. Their lightweight frames and modern designs make them a top choice for urban commuters and fitness enthusiasts alike."""
    }
    return responses.get(intent, "I'm not sure how to respond to that.")

# Chatbot interaction
def chatbot():
    user_input = input("You: ")
    tokens = tokenize_input(user_input)
    pos_tags = pos_tagging(tokens)
    lemmatized_tokens = lemmatize_tokens(pos_tags)
    intent = detect_intent(lemmatized_tokens)
    response = generate_response(intent)
    print(f"Basit: {response}")

# Run the chatbot
chatbot()
