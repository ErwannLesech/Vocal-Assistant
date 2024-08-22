import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from config.conf
load_dotenv(dotenv_path="config.conf")

# Initialize OpenAI client
client = OpenAI()

def get_written_response(prompt):
    try:
        # Create a chat completion request
        completion = client.chat.completions.create(
            model="gpt-4o",  # Ensure this is the correct model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        
        # Extract and return the response text
        return completion.choices[0].message.content.strip()
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None