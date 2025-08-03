import os
import openai
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Ensure key is in .env or system env

def chat_completion_function(messages):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0.5
    )
    return response.choices[0].message.content
