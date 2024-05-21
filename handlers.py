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
