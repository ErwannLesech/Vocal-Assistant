import pyaudio
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
        waveFile.close()