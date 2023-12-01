from input import get_input
from whisper import get_transcript

audio_file = "input.wav"

def main():
    get_input(audio_file)
    transcript = get_transcript(audio_file)
    print(transcript)

main()