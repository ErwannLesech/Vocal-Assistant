from dotenv import load_dotenv
import openai
import os

load_dotenv(dotenv_path="config.conf")

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are my personal vocal assistant."},
            {"role": "user", "content": prompt}
            ],
        temperature=0.9,
        max_tokens=150,
    )
    
    return response["choices"][0]["message"]["content"]