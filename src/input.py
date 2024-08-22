"""import pyaudio
import wave

audio = pyaudio.PyAudio()

stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

frames = []

def get_input(audio_file):
    
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
        waveFile.close()"""

import pyttsx3
import speech_recognition as sr

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def get_audio():
    command = ''
    try:
        with sr.Microphone() as source:
            print('Adjusting for ambient noise...')
            listener.adjust_for_ambient_noise(source)
            print('Listening...')
            voice = listener.listen(source, timeout=5, phrase_time_limit=5)
            print('Processing...')
            command = listener.recognize_google(voice)
            command = command.lower()
            print(f"Recognized command: {command}")
            if 'thomas' in command:
                command = command.replace('thomas', '')
                return command
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None