"""from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_ai(message: str):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=message
    )

    return response.output_text"""

import ollama

def ask_ai(message: str):
    response = ollama.chat(
        model="llama3.2", 
        messages=[
            {
                "role": "system", 
                "content": (
                    "You are a helpful DevOps assistant." 
                    "Answer the user's questions to the best of your ability."
                )
            },
            {
                "role": "user", 
                "content": message
            }
        ]
    )
    return response["message"]["content"]