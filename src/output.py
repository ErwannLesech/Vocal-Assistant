import requests
from dotenv import load_dotenv
import os
import pygame

# Load environment variables from config.conf
load_dotenv(dotenv_path="config.conf")

# Get the API key from the environment variable
elevenLabs_key = os.getenv("ELEVENLABS_API_KEY")

# Voice ID from ElevenLabs
voice_id = "GBv7mTt0atIp3Br8iCZE"

# API URL with the voice ID
url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

# Headers for the request
headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": elevenLabs_key
}

# Function to generate and save the audio file
def generate_audio_file(prompt):
    try:
        data = {
            "text": prompt,
            "model_id": "eleven_monolingual_v1",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.5
            }
        }

        # Make the POST request to generate speech
        response = requests.post(url, json=data, headers=headers, stream=True)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Write the audio to a file
            with open('output.mp3', 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            print("Audio successfully saved to output.mp3")
        else:
            print(f"Failed to generate audio. Status code: {response.status_code}")
            print(f"Response: {response.text}")
    except Exception as e:
        print(f"Error: {e}")
    
    play_audio('output.mp3')

# Function to play the MP3 file
def play_audio(file_path):
    try:
        # Initialize pygame mixer
        pygame.mixer.init()
        # Load the MP3 file
        pygame.mixer.music.load(file_path)
        # Play the audio
        pygame.mixer.music.play()
        
        # Wait until the audio is done playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(f"Error playing audio: {e}")