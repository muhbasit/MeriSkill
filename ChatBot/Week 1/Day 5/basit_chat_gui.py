import tkinter as tk
from tkinter import scrolledtext
import requests

# Flask server URL
FLASK_SERVER_URL = "http://127.0.0.1:5000/chat"  # Adjust if running on a different host or port

# Function to send message and receive response
def send_message():
    user_input = user_input_field.get()
    if user_input:
        chat_area.config(state=tk.NORMAL)  # Enable chat area for editing
        chat_area.insert(tk.END, f"You: {user_input}\n")  # Display user message
        user_input_field.delete(0, tk.END)  # Clear the input field
        
        # Send request to Flask server
        response = requests.post(FLASK_SERVER_URL, json={"message": user_input})
        bot_response = response.json().get('response')
        
        chat_area.insert(tk.END, f"Basit: {bot_response}\n")  # Display bot response
        chat_area.config(state=tk.DISABLED)  # Disable editing to prevent user from modifying it
        chat_area.yview(tk.END)  # Scroll to the bottom of the chat area

# Function to close the application
def close_application():
    root.destroy()

# Create the main application window
root = tk.Tk()
root.title("Toutche Chatbot")
root.geometry("400x500")
root.resizable(False, False)

# Create a scrolled text area for the chat
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, height=20, font=("Calibri", 12))
chat_area.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create an entry field for user input
user_input_field = tk.Entry(root, font=("Calibri", 12), width=40)
user_input_field.grid(row=1, column=0, padx=10, pady=(0, 10))

# Create a send button
send_button = tk.Button(root, text="Send", command=send_message, font=("Calibri", 12))
send_button.grid(row=1, column=1, padx=(0, 10), pady=(0, 10))

# Create a close button
close_button = tk.Button(root, text="Close", command=close_application, font=("Calibri", 12))
close_button.grid(row=2, column=0, columnspan=2, pady=(0, 10))

# Start the application
root.mainloop()
