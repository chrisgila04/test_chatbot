import openai, os, requests,  sys
from openai import AzureOpenAI


MESSAGE_SYSTEM = "You are a skilled stand-up comedian with a quick wit and charismatic presence for telling short clever storytelling and ability to connect with diverse audiences through humor that is both insightful and relatable."
messages = [{"role": "system", "content": MESSAGE_SYSTEM}]

def to_dict(obj):
    return {
        "content": obj.content,
        "role": obj.role,
    }

def generate_chat_completion(user_input=""):
    messages.append({"role": "user", "content": user_input})
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=messages
    )
    message = completion.choices[0].message
    messages.append(to_dict(message))
    return message.content
    
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
