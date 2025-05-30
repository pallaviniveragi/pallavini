import streamlit as st
from datetime import datetime
import random


st.set_page_config(page_title="✨ SmartChat", layout="centered")

# Custom Styling
st.markdown("""
    <style>
    body {
        background-color: #f7f9fc;
        font-family: 'Segoe UI', sans-serif;
    }
    .chat-box {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 15px;
        margin: 10px 0;
        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        width: fit-content;
        max-width: 80%;
    }
    .user-msg {
        background-color: #d0ebff;
        align-self: flex-end;
        margin-left: auto;
    }
    .bot-msg {
        background-color: #e9ecef;
        align-self: flex-start;
        margin-right: auto;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("💬 SmartChat - Your Friendly Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Response Logic
def bot_reply(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return random.choice(["Hey there! 😊", "Hi! How can I help you?", "Hello! 👋"])
    elif "your name" in user_input:
        return "I'm SmartChat, your Python-powered assistant! 🤖"
    elif "time" in user_input:
        return f"🕒 It's currently {datetime.now().strftime('%I:%M %p')}."
    elif "date" in user_input:
        return f"📅 Today is {datetime.now().strftime('%A, %B %d, %Y')}."
    elif "how are you" in user_input:
        return "I'm great, thanks for asking! How can I assist you? 😄"
    elif "joke" in user_input:
        return random.choice([
            "Why did the developer go broke? Because he used up all his cache! 😂",
            "Why do Java developers wear glasses? Because they don't see sharp!",
            "Debugging: Being the detective in a crime movie where you are also the murderer."
        ])
    elif "help" in user_input:
        return "Ask me about the time, date, jokes, or just say hi!"
    elif "thank" in user_input:
        return "You're welcome! 😊"
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! 👋 Have a wonderful day!"
    else:
        return "I'm not sure how to respond to that. Try asking something else! 🤔"

# Chat Input
user_input = st.chat_input("Type a message...")

if user_input:
    # Add user message
    st.session_state.messages.append(("user", user_input))
    # Get bot reply
    reply = bot_reply(user_input)
    st.session_state.messages.append(("bot", reply))

# Chat Output
for sender, message in st.session_state.messages:
    role_class = "user-msg" if sender == "user" else "bot-msg"
    st.markdown(f"<div class='chat-box {role_class}'>{message}</div>", unsafe_allow_html=True)

