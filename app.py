# app.py
import streamlit as st
from handlers import generate_chat_completion

# Streamlit App
st.title("😂 Funny Chatbot App")  # Add a title

# User input
with st.form("user_form", clear_on_submit=True):
    user_input = st.text_input("Let me know the joke topic you`d like me to share with you")
    submit_button = st.form_submit_button(label="Send")

# Press Enter to generate response from chatbot

if submit_button:
    completion = generate_chat_completion(user_input)
    st.write(completion)
