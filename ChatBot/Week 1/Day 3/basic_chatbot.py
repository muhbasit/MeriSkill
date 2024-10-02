import re
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import numpy as np

# Download necessary NLTK resources (if not already downloaded)
nltk.download('punkt')

# Sample product-related keywords for Toutche
product_keywords = ["bicycle", "electric", "heileo", "battery", "range", "features", "price", "purchase", "support", "service"]

# Basic text preprocessing function
def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()
    # Remove punctuation using regular expressions
    text = re.sub(r'[^\w\s]', '', text)
    # Tokenize the text
    tokens = nltk.word_tokenize(text)
    return tokens

# Function to identify keywords related to Toutche's products
def identify_keywords(text):
    tokens = preprocess_text(text)
    found_keywords = [word for word in tokens if word in product_keywords]
    return found_keywords

# Expanded user queries for intent classification
training_data = [
    ("Tell me about the Heileo electric bicycle", "product_info"),
    ("What is the price of the battery?", "pricing"),
    ("I need technical support for my bicycle", "technical_support"),
    ("How long does the battery last?", "product_info"),
    ("Can you help me with my electric bike?", "technical_support"),
    ("What features does the Heileo bicycle have?", "product_info"),
    ("Where can I purchase the Heileo bicycle?", "purchase_info"),
    ("What is the range of the Heileo electric bike?", "product_info"),
    ("Do you offer any warranties on the bicycles?", "warranty_info"),
    ("I am having issues with the bike's battery", "technical_support"),
    ("Can you tell me about the different models available?", "product_info"),
    ("What are the payment options for purchasing a bicycle?", "pricing"),
    ("How do I charge the battery?", "technical_support"),
    ("Are there any discounts available for the Heileo series?", "pricing"),
    ("What is the expected delivery time for a bicycle?", "purchase_info"),
    ("I need help with my order status", "technical_support"),
]

# Tokenizing and preparing training data for intent classification
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform([text for text, label in training_data])
y_train = np.array([label for text, label in training_data])

# Train a simple logistic regression model for intent classification
model = LogisticRegression()
model.fit(X_train, y_train)

# Function to classify user queries
def classify_intent(user_input):
    X_test = vectorizer.transform([user_input])
    predicted_intent = model.predict(X_test)[0]
    return predicted_intent

# Example usage
if __name__ == "__main__":
    # Preprocess and identify keywords
    sample_text = "I want to know more about the Heileo electric bicycle features."
    keywords = identify_keywords(sample_text)
    print("Identified Keywords:", keywords)

    # Classify user intent
    user_query = "What is the price of the Heileo electric bike?"
    intent = classify_intent(user_query)
    print("Classified Intent:", intent)
