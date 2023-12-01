from elevenlabs import set_api_key
from elevenlabs import generate  
from elevenlabs import play
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="config.conf")

elevenLabs_key = os.getenv("ELEVENLABS_API_KEY")

print(elevenLabs_key)

set_api_key(elevenLabs_key)

def get_vocal_response(prompt):
    audio = generate(prompt)
    play(audio)
