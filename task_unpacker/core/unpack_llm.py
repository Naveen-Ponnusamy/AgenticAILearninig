import os
import json
import re
from langchain_core.messages import HumanMessage
from config.llm import chat_completion_function
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage
from config.settings import OPENAI_API_KEY, DEFAULT_MODEL

# Load prompt from file
def load_prompt_template():
    with open("prompts/unpack_template.txt", "r", encoding="utf-8") as f:
        return f.read()

# Create OpenAI LLM
def get_llm():
    return ChatOpenAI(
        openai_api_key=OPENAI_API_KEY,
        model=DEFAULT_MODEL,
        temperature=0.5,
        max_tokens=1500
    )

# Main task unpacking function
def unpack_tasks(input_text: str) -> dict:
    prompt_template_path = os.path.join("prompts", "unpack_template.txt")

    with open(prompt_template_path, "r", encoding="utf-8") as f:
        prompt = f.read().replace("{{INPUT}}", input_text)
    messages = [
    {"role": "system", "content": "You are a helpful assistant that unpacks vague goals into detailed tasks."},
    {"role": "user", "content": prompt}
    ]
    response = chat_completion_function(messages)
    print("DEBUG - Raw LLM Response:")
    print(response)

    # Strip code fencing if present
    if response.strip().startswith("```"):
        response = re.sub(r"^```(?:json)?\n|\n```$", "", response.strip(), flags=re.IGNORECASE)

    parsed = json.loads(response)
    return parsed

