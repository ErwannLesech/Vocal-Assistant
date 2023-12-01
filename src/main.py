import pyaudio
import wave
import openai
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="config.conf")

openai.api_key = os.getenv("OPENAI_API_KEY")

audio = pyaudio.PyAudio()

stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

audio_file = "input.wav"

frames = []

def get_input():
    try:
        while True:
            data = stream.read(1024)
            frames.append(data)
    except KeyboardInterrupt:
        print("Recording finished")
        stream.stop_stream()
        stream.close()
        audio.terminate()

        waveFile = wave.open(audio_file, 'wb')
        waveFile.setnchannels(1)
        waveFile.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        waveFile.setframerate(44100)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()

def get_transcript(audio_file):
    file = open(audio_file, "rb")
    transcript = openai.Audio.transcribe("whisper-1", file=file)
    return transcript

def process():
    get_input()
    transcript = get_transcript(audio_file)
    print(transcript)

process()